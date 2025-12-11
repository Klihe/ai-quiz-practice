import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    LANGUAGE: str = os.getenv("LANGUAGE")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
