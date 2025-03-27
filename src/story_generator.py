from fastapi import HTTPException
from openai import OpenAI
import os
from config import USE_LOCAL_OLLAMA, MODEL_NAME

if USE_LOCAL_OLLAMA:
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama" 
    )
else:
    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY")
    )

def generate_story_content(prompt: str):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        error_message = f"Generation failed: {str(e)}"
        if USE_LOCAL_OLLAMA:
            error_message += ". Ensure Ollama is running and model is pulled."
        else:
            error_message += ". Check your OpenAI API key and network connection."
        raise HTTPException(status_code=500, detail=error_message)