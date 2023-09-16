from fastapi import APIRouter
import openai
from config import settings

router = APIRouter()
openai.api_key = settings.open_api_key


@router.post("/generate-text")
async def generate_text(prompt: str):
    try:
        # Use the OpenAI API to generate text
        response = openai.Completion.create(
            engine="text-davinci-003", prompt=prompt, max_tokens=100, temperature=0.6
        )
        generated_text = response.choices[0].text

        return {"generated_text": generated_text}
    except Exception as e:
        return {"error": str(e)}
