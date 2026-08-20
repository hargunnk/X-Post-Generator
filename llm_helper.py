from dotenv import load_dotenv, find_dotenv
from langchain_groq import ChatGroq
import os

# Find the .env file
env_path = find_dotenv()
print("Using .env file:", env_path)

# Load the .env file and override any existing environment variable
load_dotenv(env_path, override=True)

# Read the API key
api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print("API Key starts with:", api_key[:15] + "...")
else:
    print("ERROR: GROQ_API_KEY not found!")

# Create the Groq LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile"
)

# Test the API
if __name__ == "__main__":
    try:
        response = llm.invoke("Hello")
        print("\nGroq Response:")
        print(response.content)
    except Exception as e:
        print("\nError:")
        print(e)