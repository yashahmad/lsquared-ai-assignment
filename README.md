# 📚 FastAPI + LLM + Supabase Setup Guide 🚀
### 🛠️ Prerequisites
    Python 3.8+
    FastAPI
    Supabase account

### 📦 Installation
```
### Clone the repository:
git clone https://github.com/yashahmad/lsquared-ai-assignment.git

### Install dependencies:
pip install -r requirements.txt

cd src
```

### ⚙️ Configuration
Create a .env file in the root directory with the following format:

### Environment Configuration
```
SUPABASE_URL=<your_supabase_url>
SUPABASE_KEY=<your_supabase_key>
DEEPSEEK_API_KEY=<your_deepseek/openai_key>
```

### 🚀 Running the Application
To start the FastAPI server, run:
```
fastapi run app.py
# OR #
uvicorn main:app --reload
```

Visit http://127.0.0.1:8000/docs to access the API documentation.
Welcome to your FastAPI application integrated with LLM and Supabase! This guide will help you set up and run your project smoothly.


#### Request 1: Create Character 
``` Request
curl -X 'POST' \
  'http://127.0.0.1:8000/api/create_character' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Bilbo Baggins",
  "detail": "Hobbit of Shire, living in fantasy world of exploring mountains"
}'
```
``` Response
{
  "id": "95bf2edd-85d0-456b-ba6f-ae504ac8b303",
  "name": "Bilbo Baggins",
  "detail": "Hobbit of Shire, living in fantasy world of exploring mountains",
  "created_at": "2025-03-27T20:34:12.545117+00:00"
}
```

#### Request 2: Generate story about character
``` Request
curl -X 'POST' \
  'http://127.0.0.1:8000/api/generate_story' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "character_name": "Bilbo Baggins",
  "character_id": "95bf2edd-85d0-456b-ba6f-ae504ac8b303"
}'
```

```Response
{
  "story": "<think>\nOkay, so I need to create a compelling story about Bilbo Baggins, the hobbit of the Shire, but set it in a fantasy world where he's exploring mountains. The user has specified that the story should include a unique setting, central conflict, meaningful resolution, and at least one surprising element.\n\nFirst, I'll start by thinking about Bilbo's usual role as a hobbit. He's known for his love of books, his independence, and his connection to the Shire. But now he's venturing into the mountains, which is a significant change from his usual quiet life in Bag End.\n\nFor the unique setting, I want something that's both adventurous but also has an element of danger or enchantment. Maybe something like ancient, misty mountains with hidden villages and enchanted trails. The presence of fairies could add some magical elements without being too over-the-top.\n\nThe central conflict needs to challenge Bilbo in a meaningful way. Perhaps he encounters some tough obstacles, maybe creatures that threaten the Shire's peace, or perhaps he faces his own fears about becoming a hero. Maybe there's a threat to the mountains themselves from outside forces like an encroaching army or magical corruption.\n\nA surprising element could be something unexpected that Bilbo uncovers along his journey. Maybe he finds a hidden treasure or learns of a prophecy that ties into the fate of the mountains, adding depth to his quest.\n\nFor the resolution, it should tie back to the Shire's safe passage but also resolve any internal conflicts Bilbo has. Perhaps he confronts his fears and ends up needing to use his skills as a hobbit to save the day.\n\nNow, structuring this into chapters:\n\n1. Introduction of Bilbo in the mountains.\n2. Encounters with creatures or hidden dangers.\n3. A twist revealing an unexpected threat.\n4. Bilbo's internal conflict about becoming a hero.\n5. A major discovery that changes his perspective.\n6. The final confrontation and resolution.\n\nI need to make sure each chapter builds tension, introduces new elements, and leads to the climax where Bilbo faces the central conflict with newfound understanding or strength.\n\nPotential challenges: Making sure the setting is truly unique without being cliché; ensuring the central conflict isn't too trivial but also not overwhelming. The surprising element should feel earned rather than forced.\n\nI'll start drafting each chapter step by step, making sure to include dialogues that reflect Bilbo's personality and the interactions with",
  "character": "Bilbo Baggins",
  "model": "deepseek-r1:latest",
  "environment": "local"
}
```