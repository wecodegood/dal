import os
import re
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("DEEPSEEK_EMAIL")
password = os.getenv("DEEPSEEK_PASSWORD")


def validate_email(email):
    if not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password(password):
    if not password:
        return False
    if len(password) < 6:
        return False
    return True


def get_credentials():
    if not email:
        raise ValueError(
            "DEEPSEEK_EMAIL not set. Create a .env file based on .env.example:\n"
            "  cp .env.example .env\n"
            "Then fill in your DeepSeek account credentials."
        )

    if not password:
        raise ValueError(
            "DEEPSEEK_PASSWORD not set. Create a .env file based on .env.example:\n"
            "  cp .env.example .env\n"
            "Then fill in your DeepSeek account credentials."
        )

    if not validate_email(email):
        raise ValueError(f"Invalid email format: {email}")

    if not validate_password(password):
        raise ValueError("Password must be at least 6 characters long.")

    return email, password
