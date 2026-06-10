from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

prompt = ChatPromptTemplate.from_template(
"""
You are a professional note-taking assistant.

Create:

1. Short Summary

2. Key Points

3. Final Takeaway

Transcript:

{transcript}
"""
)

chain = prompt | llm


def generate_summary(transcript):

    response = chain.invoke(
        {
            "transcript": transcript[:12000]
        }
    )

    return response.content