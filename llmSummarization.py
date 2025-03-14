# llm_example2.py
# This example demonstrates how to use a Hugging Face summarization pipeline.
from transformers import pipeline

def main():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    text = (
        "Artificial intelligence has evolved rapidly over the past decade, "
        "leading to breakthroughs in various fields such as healthcare, finance, "
        "and technology. These advancements are largely driven by innovative machine "
        "learning techniques and deep neural networks."
    )
    summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
    print("Original Text:")
    print(text)
    print("\nSummarized Text:")
    print(summary[0]['summary_text'])

if __name__ == "__main__":
    main()
