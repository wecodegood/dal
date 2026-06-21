import os
import shutil


def setup_credentials():
    env_file = ".env"
    env_example = ".env.example"

    if os.path.exists(env_file):
        print(f"{env_file} already exists.")
        response = input("Do you want to overwrite it? (y/N): ")
        if response.lower() != "y":
            print("Keeping existing .env file.")
            return

    if not os.path.exists(env_example):
        print(f"Error: {env_example} not found. Please ensure it exists.")
        return

    shutil.copy(env_example, env_file)
    print(f"Created {env_file} from {env_example}")
    print("Please edit .env with your DeepSeek account credentials:")
    print("  DEEPSEEK_EMAIL=your-email@example.com")
    print("  DEEPSEEK_PASSWORD=your-password")


if __name__ == "__main__":
    setup_credentials()
