from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from summary_service import generate_summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SummaryRequest(BaseModel):
    transcript: str


@app.get("/")
def home():
    return {
        "status": "working"
    }


@app.post("/summary")
def summarize(request: SummaryRequest):

    summary = generate_summary(
        request.transcript
    )

    return {
        "summary": summary
    }