# anthropic_claude_example2.py
# This example demonstrates using Anthropic Claude API for summarizing a piece of text.
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
    
    text_to_summarize = (
        "Artificial intelligence is reshaping the modern world. "
        "Its applications span across industries from healthcare to finance, "
        "bringing innovation and efficiency to business processes and decision-making."
    )
    
    prompt = f"\n\nHuman: Summarize the following text: {text_to_summarize}\n\nAssistant:"
    
    data = {
        "prompt": prompt,
        "model": "claude-v1",  # Adjust if a different Claude model is required
        "max_tokens_to_sample": 100,
        "temperature": 0.5,
        "stop_sequences": ["\n\nHuman:"]
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        print("Anthropic Claude Summarization:")
        print(result.get("completion", "No completion found."))
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    main()
