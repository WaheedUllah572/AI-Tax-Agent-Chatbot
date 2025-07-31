import os
from openai import OpenAI
from groq import Groq
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Initialize OpenAI and Groq clients
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Generate a response from selected model
def get_tax_agent_response(user_input, model_choice):
    prompt = f"""
You are a multilingual, global AI Tax Agent.
You can answer tax-related questions for any country including Pakistan, India, UK, USA, Canada, etc.
Use only the user's question to infer the country.
If the country isn't clear, give a general answer and recommend checking with a local expert.

Question:
{user_input}
"""

    if "OpenAI" in model_choice:
        response = openai_client.chat.completions.create(
            model="gpt-4" if "4" in model_choice else "gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI tax advisor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()

    elif "Groq" in model_choice:
        chat_response = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "You are a helpful AI tax advisor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0
        )
        return chat_response.choices[0].message.content.strip()

    else:
        return "❌ Model not supported. Please select OpenAI or Groq."
