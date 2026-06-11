# # import os

# # print("GROQ KEY:", os.getenv("GROQ_API_KEY"))

# # from dotenv import load_dotenv
# # from langchain_groq import ChatGroq
# # from langchain_core.prompts import ChatPromptTemplate

# # load_dotenv()

# # llm = ChatGroq(
# #     model="llama-3.1-8b-instant"
# # )

# # prompt = ChatPromptTemplate.from_template(
# # """
# # You are an expert YouTube video summarizer.

# # Transcript:
# # {transcript}

# # Generate:
# # 1. Short Summary
# # 2. Key Takeaways
# # 3. Important Concepts
# # """
# # )

# # chain = prompt | llm

# # def generate_summary(transcript):

# #     result = chain.invoke(
# #         {
# #             "transcript": transcript
# #         }
# #     )

# #     return result.content


# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# # from langchain_groq import ChatGroq
# # import os

# # llm = ChatGroq(
# #     model="llama-3.1-8b-instant",  # fast + good for summarization
# #     api_key=os.getenv("GROQ_API_KEY")
# # )

# # def generate_summary(transcript: str):

# #     # STEP 1: chunk transcript
# #     splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=2000,
# #         chunk_overlap=200
# #     )

# #     chunks = splitter.split_text(transcript)

# #     # STEP 2: summarize each chunk
# #     chunk_summaries = []

# #     for chunk in chunks:
# #         res = llm.invoke(f"""
# # You are an expert YouTube video summarizer.

# # Summarize this part clearly in simple bullet points:

# # {chunk}
# # """)
# #         chunk_summaries.append(res.content)

# #     # STEP 3: final summary
# #     combined = "\n".join(chunk_summaries)

# #     final = llm.invoke(f"""
# # Create a clean structured YouTube video summary.

# # Include:
# # - Main idea
# # - Key points
# # - Important insights

# # Content:
# # {combined}
# # """)

# #     return final.content


# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain_groq import ChatGroq
# import os

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     api_key=os.getenv("GROQ_API_KEY")
# )


# # def generate_summary(transcript: str):

# #     # 🚨 STEP 0: VALIDATION (IMPORTANT FIX)
# #     if not transcript or len(transcript.strip()) < 100:
# #         return "❌ Transcript too short or invalid. Cannot generate meaningful summary."

# #     # STEP 1: split transcript safely
# #     splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=2000,
# #         chunk_overlap=200
# #     )

# #     chunks = splitter.split_text(transcript)

# #     # STEP 2: chunk summarization
# #     chunk_summaries = []

# #     for chunk in chunks:
# #         try:
# #             res = llm.invoke(f"""
# # You are an expert YouTube video summarizer.

# # RULES:
# # - Only use given content
# # - No guessing
# # - No templates
# # - Be precise and structured

# # TASK:
# # Summarize this part in bullet points:

# # {chunk}
# # """)

# #             chunk_summaries.append(res.content)

# #         except Exception as e:
# #             chunk_summaries.append(f"Chunk failed: {str(e)}")

# #     # STEP 3: combine safely
# #     combined = "\n".join(chunk_summaries)

# #     # STEP 4: final summary
# #     try:
# #         final = llm.invoke(f"""
# # You are an expert YouTube video analyst.

# # Create a FINAL structured summary:

# # FORMAT:
# # - Main Idea
# # - Key Points (bullet points)
# # - Important Insights

# # STRICT RULES:
# # - Do NOT add placeholders
# # - Do NOT ask questions
# # - Do NOT assume missing info
# # - Use only provided content

# # CONTENT:
# # {combined}
# # """)

# #         return final.content

# #     except Exception as e:
# #         return f"❌ Final summarization failed: {str(e)}"

# def generate_summary(transcript: str):

#     print("GENERATE SUMMARY CALLED")
#     print("TRANSCRIPT SIZE:", len(transcript))

#     splitter = RecursiveCharacterTextSplitter(
#     chunk_size=8000,
#     chunk_overlap=200
# )

#     chunks = splitter.split_text(transcript)

#     print("TOTAL CHUNKS:", len(chunks))

#     chunk_summaries = []

#     for i, chunk in enumerate(chunks):
#         print(f"PROCESSING CHUNK {i+1}/{len(chunks)}")

#         res = llm.invoke(f"""
# You are an expert YouTube video summarizer.

# Summarize this part clearly in simple bullet points:

# {chunk}
# """)

#         print("CHUNK RESPONSE RECEIVED")

#         chunk_summaries.append(res.content)

#     combined = "\n".join(chunk_summaries)

#     print("FINAL SUMMARY GENERATION STARTED")

#     final = llm.invoke(f"""
# Create a clean structured YouTube video summary.

# Include:
# - Main idea
# - Key points
# - Important insights

# Content:
# {combined}
# """)

#     print("FINAL SUMMARY GENERATED")

#     return final.content 

from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")
)

# def generate_summary(transcript: str):

#     print("GENERATE SUMMARY CALLED")
#     print("TRANSCRIPT SIZE:", len(transcript))

#     # Prevent huge prompts
#     transcript = transcript[:5000]

#     print("TRUNCATED SIZE:", len(transcript))

#     response = llm.invoke(f"""
# You are an expert YouTube video summarizer.

# IMPORTANT RULES:
# - Always generate the summary in English.
# - Even if the transcript is in Hindi or any other language, first understand it and then write the summary in English.
# - Keep the summary concise and easy to read.
# - Use proper headings and bullet points.

# Create a structured summary using the following format:

# # Main Idea
# (2-3 sentences)

# # Key Points
# - Point 1
# - Point 2
# - Point 3
# - Point 4
# - Point 5

# # Important Insights
# - Insight 1
# - Insight 2
# - Insight 3

# Transcript:
# {transcript}
# """)

#     print("SUMMARY GENERATED")

#     return response.content


def generate_summary(transcript: str):

    print("GENERATE SUMMARY CALLED")

    transcript = transcript[:5000]

    print("TRANSCRIPT AFTER CUT:", len(transcript))

    try:
        response = llm.invoke(f"""
You are an expert YouTube video summarizer.

IMPORTANT:
- Read and understand the transcript regardless of its language.
- ALWAYS generate the final summary in English.
- If the transcript is in Hindi, translate the ideas to English before summarizing.
- Never write the final answer in Hindi.
- Use clear headings and bullet points.

Provide the summary in this format:

# Main Idea

# Key Points
- Point 1
- Point 2
- Point 3
- Point 4
- Point 5

# Important Insights
- Insight 1
- Insight 2
- Insight 3

Transcript:
{transcript}
""")

        print("GROQ RESPONSE RECEIVED")

        return response.content

    except Exception as e:
        print("GROQ ERROR:", e)
        raise e