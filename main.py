import os, argparse, json
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_functions import available_functions
from functions.write_file import write_file
from functions.get_file_content import get_file_content


def main():
    ### CLI ###
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    
    # Get user input for message to agent
    args = parser.parse_args()
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    ### CONNECT TO OPENROUTER ###
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("could not find API key in .env")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions,
    )

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    if response.usage is None:
        raise RuntimeError("Possible API request failure. No usage property in API response.")
    
    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or {})
            print(f"Calling function: {tool_call.function.name}({function_args})")
    
    print("Response:\n")
    print(response.choices[0].message.content)
    # print("\nTool Calls:\n")
    # print(message.tool_calls)


    # logging attempt
    # print(response)
    past_responses = get_file_content(".", "responses.txt", no_max=True)
    past_responses += "\n" + str(response) + "\n######"
    write_file(".", "responses.txt", past_responses)
    # end logging


if __name__ == "__main__":
    main()
