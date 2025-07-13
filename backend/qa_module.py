# backend/qa_module.py

from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

# Load sentence embedding model
embedder = SentenceTransformer('all-MiniLM-L6-v2')  # small, fast
# Load summarization pipeline for final answer
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def build_context_index(document_text, chunk_size=500):
    """
    Split document into chunks, encode each chunk to build a similarity search index.
    """
    chunks = []
    text = document_text
    while text:
        if len(text) <= chunk_size:
            chunks.append(text)
            break
        split_pos = text.rfind('. ', 0, chunk_size)
        if split_pos == -1:
            split_pos = chunk_size
        else:
            split_pos += 1
        chunks.append(text[:split_pos])
        text = text[split_pos:].lstrip()
    # Compute embeddings
    embeddings = embedder.encode(chunks, convert_to_tensor=True)
    return chunks, embeddings

def answer_question(question, chunks, embeddings):
    """
    Given a user question, find the most similar chunk and summarize it into an answer.
    """
    question_embedding = embedder.encode(question, convert_to_tensor=True)
    scores = util.cos_sim(question_embedding, embeddings)[0]
    best_idx = scores.argmax()
    best_chunk = chunks[best_idx]

    # Now turn the best chunk into a summary as an answer
    summary = summarizer_pipeline(best_chunk, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    return summary, best_chunk
