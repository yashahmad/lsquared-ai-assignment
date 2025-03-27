from fastapi import HTTPException, status
from uuid import uuid4
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

async def create_character(character):
    try:
        new_char = {
            "id": str(uuid4()),
            "name": character.name,
            "detail": character.detail
        }
        
        response = supabase.table('characters').insert(new_char).execute()
        
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create character"
            )
            
        return response.data[0]
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )

def get_character(character_id: str = None, character_name: str = None):
    try:
        if character_id:
            response = supabase.table('characters').select('*').eq('id', character_id).execute()
        elif character_name:
            response = supabase.table('characters').select('*').eq('name', character_name).execute()
        else:
            return None
            
        if not response.data:
            return None
        return response.data[0]
        
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error: {str(e)}"
        )