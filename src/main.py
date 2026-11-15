from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file

def main():
    print("Hello, LangChain Course 3!")
    print("GEMINI_API_KEY:", os.getenv("GEMINI_API_KEY"))

if __name__ == "__main__":
    main()