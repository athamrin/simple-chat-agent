import os
from openai import OpenAI
from dotenv import load_dotenv


def call_ai(user_input:str, openrouter_api_key:str, openrouter_base_url, openrouter_model:str) -> None:
    try:
        client = OpenAI(api_key=openrouter_api_key, base_url=openrouter_base_url)
        response = client.responses.create(
            model=openrouter_model,
            input=user_input,
        )
        print(response.output_text)
    except Exception as e:
        print(f"An error occured: {e}")

def main() -> None:
    load_dotenv()
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    openrouter_base_url = os.getenv("OPENROUTER_BASE_URL")
    openrouter_model = os.getenv("OPENROUTER_MODEL")
    
    print(f"This is a chat terminal for communicating with A.I. model {openrouter_model.split("/")[1].replace("-", " ")}")
    while True:
        user_input = input("Your input (Type 'keluar' to exit): ")
        if user_input.strip().lower() == 'keluar':
            break
        call_ai(user_input, openrouter_api_key, openrouter_base_url, openrouter_model)

if __name__ == "__main__":
    main()

