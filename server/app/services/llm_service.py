import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_groq import ChatGroq
from langchain.agents import create_react_agent, AgentExecutor 
from langchain.tools import Tool
from langchain_core.messages import HumanMessage, SystemMessage
from langchain import hub

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(current_dir,"..", "db", "chroma_db")

embeddings_model = HuggingFaceBgeEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
db = Chroma(persist_directory=persistent_directory, embedding_function=embeddings_model)

def query_vector_store(query: str):
    retriever = db.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.4}
    )
    relevant_docs = retriever.invoke(query)
    if not relevant_docs:
        return "No relevant documents found."
    return "\n\n".join([doc.page_content for doc in relevant_docs])



def get_llm_agent_response(user_query: str):
    
    query_tool = Tool(
        name="Query Vector Store",
        func=query_vector_store,
        description="Use this tool to retrieve relevant documents from the vector store for the topic sound"
    )

    prompt = hub.pull("hwchase17/react")
    model = ChatGroq(model="llama3-8b-8192",api_key=os.getenv("GROQ_API_KEY"))

    tools = [query_tool]
    agent = create_react_agent(llm=model, tools=tools, prompt=prompt, stop_sequence=True)

    agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
    response = agent_executor.invoke({"input": user_query})

    return response

def get_llm_response(user_query:str):

    relevant_docs = query_vector_store(user_query)

    template = (
         "Here are some documents that might help answer the question: "
    + user_query
    + "\n\n Relevant Documents:\n"
    + "\n\n".join(relevant_docs)
    + "\n\n Please provide an answer based only on the provided documents. If the answer is not found in the documents, respond with 'I'm not sure. Please ask questions relevant to the topic'."
    + "\n\n Keep it concise you should only return the answer. dont include the question" + user_query + "in the result and also don't include reevant docs. and no kind of thing should be returned and strictly no bluff and don't return any note"
    )

    model = ChatGroq(model="llama3-8b-8192",api_key=os.getenv("GROQ_API_KEY"))

    messages = [
        SystemMessage("You are a helpful assistant."),
        HumanMessage(template)
    ]

    result = model.invoke(messages)

    return result.content



