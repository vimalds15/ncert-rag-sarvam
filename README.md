# Sarvam.ai Assignment - Anto Vimalan S

A webapp to get your doubts solved using AI (limited to NCERT book and Sound Chapter)

## A bit about Myself and thought process

Already Known: Frontend part
Learned: FastAPI, RAG, Agent, LLM, Tool Calling etc.,

Basicaly I learned everything related to backend part of this project 

### Step by Step Breakdown:

- Watched YouTube videos and blogs to understand RAG, LLM, Agents etc., 
- Implemented some examples to practically understand how it works
- After a good hold, started to break down the tasks
- Part 1: Converting PDF to text -> text to embeddings -> embeddings to store in vectorDB
- Part 2: Using RAG to query VectorDB and it's tuning
- Part 3: Using Agent and tool calling to query VectorDB  



## Tech Stack
- FrontEnd: React, Tailwind CSS, Vite
- Backend: FastAPI
- LLM: Groq Llama
- Vector DB: ChromaDB
- Embeddings: HuggingFace

## User Journey

1. If Default Option is selected it will perform querying VectorDB and returns the result

2. If Agent Option is selected it will use AI Agent and tool calling and returns the result

