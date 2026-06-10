from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="llama3-8b-8192"
)

prompt = ChatPromptTemplate.from_template(
"""
You are an expert YouTube video summarizer.

Transcript:
{transcript}

Generate:
1. Short Summary
2. Key Takeaways
3. Important Concepts
"""
)

chain = prompt | llm

def generate_summary(transcript):

    result = chain.invoke(
        {
            "transcript": transcript
        }
    )

    return result.content