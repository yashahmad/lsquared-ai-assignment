from pydantic import BaseModel

class CharacterCreate(BaseModel):
    name: str
    detail: str

class StoryGenerate(BaseModel):
    character_name: str | None = None
    character_id: str | None = None