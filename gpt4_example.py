# gpt4_example.py
# This example demonstrates how to use OpenAI's GPT-4 API to generate responses.

import os
import openai

def main():
    # Set your OpenAI API key from the environment variable
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY is not set. Please set it in your environment variables.")

    prompt = "Explain the significance of prompt engineering for large language models."
    
    # Call the GPT-4 API via the ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a knowledgeable assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        temperature=0.7
    )
    print("GPT-4 Response:")
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
