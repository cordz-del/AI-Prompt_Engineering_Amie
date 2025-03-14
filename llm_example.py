# llm_example.py
# This example demonstrates how to use a generic large language model from Hugging Face Transformers.

from transformers import pipeline

def main():
    # Load a pre-trained model (e.g., GPT-2) for text generation
    generator = pipeline('text-generation', model='gpt2')
    prompt = "Once upon a time in a futuristic world,"
    output = generator(prompt, max_length=50, num_return_sequences=1)
    print("Generated Text:")
    print(output[0]['generated_text'])

if __name__ == "__main__":
    main()
