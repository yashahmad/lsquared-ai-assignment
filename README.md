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
