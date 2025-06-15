import os
import sys
from google import genai
from google.genai import types
from dotenv import load_dotenv

def main():
    load_dotenv()

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <prompt>")
        sys.exit(1)

    user_prompt = sys.argv[1]

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            generate_content_verbose(client, messages, user_prompt)
    else: 
        generate_content(client, messages)


def generate_content(client, messages):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages
    )
    print("Response:")
    print(response.text)

def generate_content_verbose(client, messages, user_prompt):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages
    )
    print(f"User prompt:\n{user_prompt}")
    print("Response:")
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()


