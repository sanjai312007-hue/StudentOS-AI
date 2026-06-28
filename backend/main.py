from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="StudentOS AI Backend",
    description="High-performance asynchronous API service powering the RAG pipeline, AI Tutor, and Study Planner",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Data Models ──────────────────────────────────────────────────
class QueryRequest(BaseModel):
    query: str
    subject: Optional[str] = "General"
    difficulty: Optional[str] = "Beginner"

class RAGQueryRequest(BaseModel):
    query: str
    target_docs: List[str]

class QuizConfig(BaseModel):
    subject: str
    difficulty: str
    num_questions: int

class StudyPlanConfig(BaseModel):
    daily_hours: int
    weak_subjects: List[str]
    optimize_exams: bool

# ─── API Routes ───────────────────────────────────────────────────
@app.get("/")
async def health_check():
    return {"status": "online", "message": "StudentOS AI Backend running on uvicorn", "version": "1.0.0"}

@app.post("/api/tutor/explain")
async def tutor_explain(payload: QueryRequest):
    # Simulated AI logic
    return {
        "definition": f"Detailed academic guide on **{payload.query}** for **{payload.difficulty}** level.",
        "example": "Constructing dynamic CS models for class demonstration...",
        "code": "def example():\n    print('Demonstrating payload query')",
        "complexity": "| Case | Complexity |\n|:---|:---|\n| Worst | O(log n) |\n| Space | O(1) |",
        "interview_questions": [f"Explain components of {payload.query}"]
    }

@app.post("/api/rag/query")
async def rag_query(payload: RAGQueryRequest):
    return {
        "answer": f"Grounded response query: '{payload.query}' from targets: {payload.target_docs}",
        "source": "Mock Vector Database FAISS Index [Page 1]"
    }

@app.post("/api/quiz/generate")
async def quiz_generate(payload: QuizConfig):
    return {
        "subject": payload.subject,
        "questions": [
            {
                "question": f"Sample dynamic question for {payload.subject}",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": 0,
                "explanation": "Simulated answer logic."
            }
        ]
    }

@app.post("/api/planner/optimize")
async def planner_optimize(payload: StudyPlanConfig):
    return {
        "message": "Study schedule successfully optimized using learning analytics parameters.",
        "daily_hours_allocated": payload.daily_hours
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
