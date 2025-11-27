from openai import OpenAI
from ds1000_eval.config import Config

client = OpenAI(api_key=Config.OPENAI_API_KEY)

def generate_code(prompt: str) -> str:
    """Call the hosted LLM to generate Python code."""
    
    response = client.chat.completions.create(
        model=Config.MODEL_NAME,
        messages=[
            {"role": "system", "content": "You generate only Python code."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

