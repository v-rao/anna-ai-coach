from openai import OpenAI
import os

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt: str) -> str:
    """
    Calls GPT to generate a response using the new OpenAI API.
    """
    resp = client.chat.completions.create(
        model="gpt-4o-mini",  # Or "gpt-4o" / "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are Anna, a helpful startup coach for first-time entrepreneurs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return resp.choices[0].message.content.strip()

