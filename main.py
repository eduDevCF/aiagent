import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


def main():
    ### CLI ###
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    # Get user input for message to agent
    args = parser.parse_args()
    messages = [
        {"role": "user", "content": args.user_prompt},
    ]

    ### CONNECT TO OPENROUTER ###
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key is None:
        raise RuntimeError("could not find API key in .env")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    if response.usage is None:
        raise RuntimeError("Possible API request failure. No usage property in API response.")
    
    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
