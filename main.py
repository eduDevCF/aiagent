import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


def main():
    ### CLI ###
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    # Get user input for message to agent
    args = parser.parse_args()

    # print(args.user_prompt)

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
        messages=[
            {
                "role": "user",
                "content": args.user_prompt,
            }
        ],
    )
    if response.usage != None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("Possible API request failure. No usage property in API response.")
    
    print("Response:")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
