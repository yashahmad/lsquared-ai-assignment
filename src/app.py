from fastapi import FastAPI, HTTPException, status
from models import CharacterCreate, StoryGenerate
from database import create_character, get_character
from story_generator import generate_story_content
from config import USE_LOCAL_OLLAMA, MODEL_NAME

app = FastAPI()

@app.post("/api/create_character", status_code=status.HTTP_201_CREATED)
async def create_character_endpoint(character: CharacterCreate):
    return await create_character(character)

@app.post("/api/generate_story", status_code=status.HTTP_201_CREATED)
async def generate_story(request: StoryGenerate):
    try:
        character = None
        if request.character_id:
            character = get_character(character_id=request.character_id)
        elif request.character_name:
            character = get_character(character_name=request.character_name)
        
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")

        prompt = f"""Create a compelling story about {character['name']}, 
        who is {character['detail']}. Include:
        - A unique setting
        - A central conflict
        - A meaningful resolution
        - At least one surprising element"""
        
        story = generate_story_content(prompt)
        return {
            "story": story,
            "character": character["name"],
            "model": MODEL_NAME,
            "environment": "local" if USE_LOCAL_OLLAMA else "production"
        }
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Server error: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)