# anthropic_claude_example3.py
# This example uses Anthropic Claude API to generate a conversational reply.
import os
import requests
import json

def main():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY is not set.")

    url = "https://api.anthropic.com/v1/complete"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key
    }
    
    # A conversation-like prompt for Claude
    prompt = (
        "\n\nHuman: I'm feeling a bit anxious about my upcoming presentation. What should I do?\n\nAssistant:"
    )
    
    data = {
        "prompt": prompt,
        "model": "claude-v1",
        "max_tokens_to_sample": 150,
        "temperature": 0.7,
        "stop_sequences": ["\n\nHuman:"]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        print("Anthropic Claude Conversational Response:")
        print(result.get("completion", "No completion found."))
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    main()
