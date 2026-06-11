# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# from summary_service import generate_summary

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class SummaryRequest(BaseModel):
#     transcript: str


# @app.get("/")
# def home():
#     return {
#         "status": "working"
#     }


# @app.post("/summary")
# def summarize(request: SummaryRequest):

#     summary = generate_summary(
#         request.transcript
#     )

#     return {
#         "summary": summary
#     }



# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# from summary_service import generate_summary

# app = FastAPI()   # ✅ MUST BE UNCOMMENTED

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class SummaryRequest(BaseModel):
#     transcript: str


# @app.get("/")
# def home():
#     return {"status": "working"}


# @app.post("/summary")
# def summarize(request: SummaryRequest):
#     summary = generate_summary(request.transcript)
#     return {"summary": summary}


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from fastapi.responses import JSONResponse

# from summary_service import generate_summary

# app = FastAPI()

# # CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class SummaryRequest(BaseModel):
#     transcript: str

# @app.get("/")
# def home():
#     return {"status": "working"}

# @app.post("/summary")
# def summarize(request: SummaryRequest):

#     try:
#         summary = generate_summary(request.transcript)

#         return JSONResponse(content={
#             "summary": summary
#         })

#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={
#                 "error": str(e)
#             }
#         ) 


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from fastapi.responses import JSONResponse

# from transcript_service import get_transcript
# from summary_service import generate_summary

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class SummaryRequest(BaseModel):
#     video_id: str

# @app.get("/")
# def home():
#     return {"status": "working"}

# @app.post("/summary")
# def summarize(request: SummaryRequest):

#     try:
#         transcript = get_transcript(request.video_id)

#         if transcript.startswith("ERROR"):
#             return JSONResponse(
#                 status_code=400,
#                 content={"error": "Transcript not available"}
#             )

#         summary = generate_summary(transcript)

#         return JSONResponse(content={"summary": summary})

#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={"error": str(e)}
#         )

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from fastapi.responses import JSONResponse

# from summary_service import generate_summary
# from transcript_service import get_transcript

# app = FastAPI()

# # CORS setup
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Request model
# class SummaryRequest(BaseModel):
#     video_id: str


# @app.get("/")
# def home():
#     return {"status": "Backend is running"}


# @app.post("/summary")
# def summarize(request: SummaryRequest):

#     try:
#         print("DEBUG VIDEO ID:", request.video_id)

#         transcript = get_transcript(request.video_id)

#         # 🚨 STRICT CHECK (VERY IMPORTANT)
#         if not transcript or len(transcript.strip()) < 100:
#             return {
#                 "summary": "❌ Not enough transcript available to generate a meaningful summary for this video."
#             }

#         summary = generate_summary(transcript)

#         return {
#             "summary": summary
#         }

#     except Exception as e:
#         return {
#             "summary": f"Error: {str(e)}"
#         }
    
    
# transcript = get_transcript(request.video_id)

# print("TRANSCRIPT LENGTH:", len(transcript) if transcript else 0)

# if transcript:
#     print(transcript[:500]) 


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from summary_service import generate_summary
from transcript_service import get_transcript

app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class SummaryRequest(BaseModel):
    video_id: str


@app.get("/")
def home():
    return {"status": "Backend is running"}


@app.post("/summary")
def summarize(request: SummaryRequest):

    try:
        print("DEBUG VIDEO ID:", request.video_id)

        # Get transcript
        transcript = get_transcript(request.video_id)

        # Debug logs
        print("TRANSCRIPT LENGTH:", len(transcript) if transcript else 0)

        if transcript:
            print("TRANSCRIPT PREVIEW:")
            print(transcript[:500])

        # Validation
        if not transcript or len(transcript.strip()) < 100:
            return {
                "summary": "❌ Not enough transcript available to generate a meaningful summary for this video."
            }

        # Generate summary
        summary = generate_summary(transcript)

        return {
            "summary": summary
        }

    except Exception as e:
        print("ERROR:", str(e))

        return {
            "summary": f"Error: {str(e)}"
        }