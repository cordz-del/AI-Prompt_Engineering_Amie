# gpt4_example2.py
# This example demonstrates how to use OpenAI's GPT-4 API to summarize a given text.
import os
import openai

def main():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        raise ValueError("OPENAI_API_KEY is not set. Please set it in your environment variables.")
    
    text_to_summarize = (
        "The rise of artificial intelligence has transformed industries worldwide. "
        "From healthcare to finance, AI technologies are driving innovation and efficiency. "
        "This has led to new business models and improved decision-making processes."
    )
    
    # GPT-4 can be used with the chat completion endpoint for summarization tasks.
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes text."},
            {"role": "user", "content": f"Summarize the following text: {text_to_summarize}"}
        ],
        max_tokens=100,
        temperature=0.5
    )
    print("GPT-4 Summarization:")
    print(response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
