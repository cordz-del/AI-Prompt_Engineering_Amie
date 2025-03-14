# anthropic_claude_example.py
# This example demonstrates how to use the Anthropic Claude API to generate a response.

import os
import requests
import json

def main():
    # Set your Anthropic API key from the environment variable
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY is not set. Please set it in your environment variables.")

    url = "https://api.anthropic.com/v1/complete"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    
    # Construct a prompt for Claude. Anthropic's prompt format usually includes conversational context.
    prompt = "\n\nHuman: Explain why prompt engineering is crucial for AI systems.\n\nAssistant:"

    data = {
        "prompt": prompt,
        "model": "claude-v1",  # Replace with the specific Claude model if needed.
        "max_tokens_to_sample": 150,
        "temperature": 0.7,
        "stop_sequences": ["\n\nHuman:"]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        print("Anthropic Claude Response:")
        print(result.get("completion", "No completion found."))
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    main()
