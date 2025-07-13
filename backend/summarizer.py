# backend/summarizer.py

from transformers import pipeline

# Load once globally (only once per session)
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_length=1000):
    """
    Split long text into chunks at sentence boundaries.
    """
    chunks = []
    while text:
        if len(text) <= max_length:
            chunks.append(text)
            break
        split_pos = text.rfind('. ', 0, max_length)
        if split_pos == -1:
            split_pos = max_length
        else:
            split_pos += 1
        chunks.append(text[:split_pos])
        text = text[split_pos:].lstrip()
    return chunks

def summarize_text(text):
    """
    Summarize a given text chunk to about 150 words using Hugging Face BART.
    """
    summary_list = summarizer_pipeline(
        text,
        max_length=150,
        min_length=50,
        do_sample=False
    )
    return summary_list[0]['summary_text']
