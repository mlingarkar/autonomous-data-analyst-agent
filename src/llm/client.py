from openai import OpenAI
from src.config import Config


def ask_llm(prompt: str) -> str:
    """
    Send a prompt to the OpenAI model and return the text response.
    """
    if not Config.OPENAI_API_KEY:
        raise ValueError(
            "OPENAI_API_KEY was not found. Check that your .env file is in the project root "
            "and contains OPENAI_API_KEY=your_key"
        )

    client = OpenAI(api_key=Config.OPENAI_API_KEY)

    response = client.chat.completions.create(
        model=Config.OPENAI_MODEL,
        temperature=Config.TEMPERATURE,
        messages=[
            {"role": "system", "content": "You are a helpful senior data analyst."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content.strip()