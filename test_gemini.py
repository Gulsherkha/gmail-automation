import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env file
load_dotenv()

# Check key
api_key = os.getenv("GOOGLE_API_KEY")
print("Gemini API key found:", bool(api_key))

# Initialize Gemini model with API key
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",   # stable name
    google_api_key=api_key      # force API key auth
)

# Test a simple query
response = llm.invoke("Hello Gemini! Can you confirm that you're working?")
print("\nGemini says:\n", response.content)
