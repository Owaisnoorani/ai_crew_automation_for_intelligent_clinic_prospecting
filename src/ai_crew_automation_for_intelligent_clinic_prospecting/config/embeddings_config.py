from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

def get_embeddings():
    return GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=os.environ["GEMINI_API_KEY"]
    ) 