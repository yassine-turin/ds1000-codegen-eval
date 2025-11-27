import os
from dotenv import load_dotenv

# Load .env if it exists
load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    MODEL_NAME = "gpt-4.1-mini"
    NUM_TASKS = 5  # default number of DS-1000 tasks to run

