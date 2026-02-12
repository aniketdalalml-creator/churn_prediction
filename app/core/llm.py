from typing import Any
from groq import Groq
from app.config import GROQ_API_KEY, LLM_MODEL

def get_llm_client():
    return Groq(api_key=GROQ_API_KEY)

def ask_llm(prompt: str) -> str:
    client = get_llm_client()

    messages: list[Any] = [
        {"role": "system", "content": "You are a telecom business analyst."},
        {"role": "user", "content": prompt}
    ]

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
        temperature=0.3
    )

    return response.choices[0].message.content
