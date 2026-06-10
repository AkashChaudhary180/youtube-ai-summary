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


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from transcript_service import get_transcript
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
    video_id: str

@app.get("/")
def home():
    return {"status": "working"}

@app.post("/summary")
def summarize(request: SummaryRequest):

    try:
        transcript = get_transcript(request.video_id)

        if transcript.startswith("ERROR"):
            return JSONResponse(
                status_code=400,
                content={"error": "Transcript not available"}
            )

        summary = generate_summary(transcript)

        return JSONResponse(content={"summary": summary})

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )