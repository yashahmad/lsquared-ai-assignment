import os
from dotenv import load_dotenv

load_dotenv()

USE_LOCAL_OLLAMA = os.getenv("USE_LOCAL_OLLAMA", "False").lower() == "true"
MODEL_NAME = os.getenv("MODEL_NAME", "deepseek-r1:latest")