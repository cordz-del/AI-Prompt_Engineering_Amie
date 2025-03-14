# gpt4_example3.py
# This example simulates a multi-turn conversation with GPT-4, showcasing context handling.
import os
import openai

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY is not set.")
    
    conversation = [
        {"role": "system", "content": "You are Amie, a compassionate and insightful assistant."},
        {"role": "user", "content": "Hi Amie, I'm feeling a bit overwhelmed today."},
        {"role": "assistant", "content": "I'm sorry to hear that. Can you tell me what's been stressing you out?"}
    ]
    
    # Continue the conversation with GPT-4
    conversation.append({"role": "user", "content": "I have too many deadlines and I don't know where to start."})
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation,
        max_tokens=150,
        temperature=0.7
    )
    
    print("GPT-4 Conversation Simulation:")
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
