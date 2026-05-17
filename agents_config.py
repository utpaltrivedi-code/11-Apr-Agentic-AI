import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

def get_llm():
    return ChatOpenAI(
        model=os.getenv("LLM_MODEL_NAME", "gpt-4o-mini"),
        temperature=0.0,
        api_key=os.getenv("OPENAI_API_KEY", "")
    )

CATEGORIES = ["Bug", "Feature Request", "Praise", "Complaint", "Spam"]
PRIORITIES = ["Critical", "High", "Medium", "Low"]