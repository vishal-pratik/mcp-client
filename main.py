import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)

response = client.responses.create(
  model="gpt-5-nano",
  input="who is president of united states ? Answer in 1 line",
  store=True,
)

print(response.output_text)
