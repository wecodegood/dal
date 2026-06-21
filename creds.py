import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("DEEPSEEK_EMAIL")
password = os.getenv("DEEPSEEK_PASSWORD")

if not email or not password:
    raise ValueError(
        "Missing credentials. Create a .env file based on .env.example:\n"
        "  cp .env.example .env\n"
        "Then fill in your DeepSeek account credentials."
    )
