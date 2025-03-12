from langchain_google_genai import ChatGoogleGenerativeAI
import os

def get_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.environ["GEMINI_API_KEY"],
        temperature=0.7,
        convert_system_message_to_human=True
    ) 