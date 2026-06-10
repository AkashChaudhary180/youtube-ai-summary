# import os

# print("GROQ KEY:", os.getenv("GROQ_API_KEY"))

# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.prompts import ChatPromptTemplate

# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.1-8b-instant"
# )

# prompt = ChatPromptTemplate.from_template(
# """
# You are an expert YouTube video summarizer.

# Transcript:
# {transcript}

# Generate:
# 1. Short Summary
# 2. Key Takeaways
# 3. Important Concepts
# """
# )

# chain = prompt | llm

# def generate_summary(transcript):

#     result = chain.invoke(
#         {
#             "transcript": transcript
#         }
#     )

#     return result.content


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",  # fast + good for summarization
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_summary(transcript: str):

    # STEP 1: chunk transcript
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )

    chunks = splitter.split_text(transcript)

    # STEP 2: summarize each chunk
    chunk_summaries = []

    for chunk in chunks:
        res = llm.invoke(f"""
You are an expert YouTube video summarizer.

Summarize this part clearly in simple bullet points:

{chunk}
""")
        chunk_summaries.append(res.content)

    # STEP 3: final summary
    combined = "\n".join(chunk_summaries)

    final = llm.invoke(f"""
Create a clean structured YouTube video summary.

Include:
- Main idea
- Key points
- Important insights

Content:
{combined}
""")

    return final.content