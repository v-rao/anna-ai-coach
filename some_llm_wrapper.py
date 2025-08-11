import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_llm(prompt: str) -> str:
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Anna, a helpful startup coach for first-time entrepreneurs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return resp.choices[0].message.content.strip()
