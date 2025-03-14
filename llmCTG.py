# llm_example3.py
# This example uses Hugging Face's GPT-2 model for creative text generation with custom parameters.
from transformers import pipeline

def main():
    generator = pipeline('text-generation', model='gpt2')
    prompt = "In a world where technology and art merge seamlessly,"
    output = generator(prompt, max_length=60, num_return_sequences=2, temperature=0.8)
    print("Generated Texts:")
    for i, result in enumerate(output):
        print(f"Sequence {i+1}: {result['generated_text']}")

if __name__ == "__main__":
    main()
