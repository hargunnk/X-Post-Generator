from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

print("Key loaded:", os.getenv("GROQ_API_KEY")[:8] + "...")

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

response = llm.invoke("Hello")
print(response.content)