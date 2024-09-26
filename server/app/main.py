from fastapi import FastAPI, HTTPException
from app.models.query_model import Question
from app.services.llm_service import get_llm_response, get_llm_agent_response
from app.services.pdf_service import process_pdf
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.on_event("startup")
async def startup_event():
    process_pdf()

@app.post("/query")
async def query_llm(question:Question):
    try:
        response = get_llm_response(question.question)
        return {"response":response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query/agent")
async def query_agent_llm(question:Question):
    try:
        response = get_llm_agent_response(question.question)
        return {"response":response["output"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))