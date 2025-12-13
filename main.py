import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types



def main():
    load_dotenv()


    try:
        parser = argparse.ArgumentParser(description="Chatbot")
        parser.add_argument("user_prompt", type=str, help="User prompt")
        parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
        args = parser.parse_args()


        api_key = os.environ.get("GEMINI_API_KEY")
        client = genai.Client(api_key=api_key)

        messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=messages
        )


        if args.verbose == True:
            print("*"*100)
            print(f"User prompt: {args.user_prompt}")
            try:
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
            except Exception as e:
                print(f"During tokens counting happened error: {e}")
            print("*"*100)


        print("Response:")
        print(response.text)

    except Exception as e:
        print(f"Error while trying to load api key: {e}")


if __name__ == "__main__":
    main()
