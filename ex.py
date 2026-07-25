import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env file
load_dotenv()

# Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",   # or any model available in your account
    google_api_key=os.getenv("FuturePath_Engine"),
    temperature=0
)

# Ask a question
question = input()

response = llm.invoke(question)

print(response.content)