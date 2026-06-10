from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from transcript_service import get_transcript
from summary_service import generate_summary

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/summary/{video_id}")
def summarize(video_id: str):

    try:

        transcript = get_transcript(video_id)

        summary = generate_summary(
            transcript
        )

        return {
            "success": True,
            "summary": summary
        }

    except Exception as e:

        print("\nERROR OCCURRED:")
        print(type(e))
        print(e)

        raise e
    
@app.get("/test")
def test():
    from youtube_transcript_api import YouTubeTranscriptApi

    api = YouTubeTranscriptApi()

    transcript = api.fetch("Op6PbJZ5b2Q", languages=["hi"])

    return {
        "length": len(transcript)
    }