import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader 
from langchain_community.vectorstores import Chroma 
from langchain_community.embeddings import HuggingFaceBgeEmbeddings

current_dir = os.path.dirname(os.path.abspath(__file__))
pdf_file_path = os.path.join(current_dir,"..","assets", "pdf", "ncert.pdf")
text_file_path = os.path.join(current_dir,"..","assets","books","ncert.txt")
persistent_directory = os.path.join(current_dir,"..","db","chroma_db")


def pdf_to_text(pdf_path, output_txt_path):
    with open(output_txt_path, "w", encoding="utf-8") as txt_file:
        reader = PdfReader(pdf_path)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            txt_file.write(page.extract_text())
def process_pdf():
    if not os.path.exists(text_file_path):
        print(f"Converting PDF {pdf_file_path} to text {text_file_path}")
        pdf_to_text(pdf_file_path, text_file_path)
        print(f"Finished converting PDF to text")

    if not os.path.exists(persistent_directory):
        print("Persistent directory does not exist. Initializing vector store")

        if not os.path.exists(text_file_path):
            raise FileNotFoundError(
                f"The file {text_file_path} does not exist. Please check the path"
            )

        loader = TextLoader(text_file_path,encoding = 'UTF-8')
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
        docs = text_splitter.split_documents(documents)

        print("\n--- Document Chunks Information ---")
        print(f"Number of document chunks: {len(docs)}")

        print("\n--- Creating embeddings ---")
        embeddings_model = HuggingFaceBgeEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
        print("\n--- Finished Creating embeddings ---")


        print("\n--- Creating vector store ---")
        db = Chroma.from_documents(
            docs, embeddings_model, persist_directory=persistent_directory
        )
        print("\n--- Finished creating vector store---")

    else:
        print("Vector store already exists. No need to initialize")
    