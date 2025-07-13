# backend/evaluator.py

from sentence_transformers import SentenceTransformer, util
from transformers import pipeline

embedder = SentenceTransformer('all-MiniLM-L6-v2')
summarizer_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def evaluate_answer(user_question, user_answer, doc_chunks, doc_embeddings):
    """
    Find the best matching snippet from the document for the question,
    and generate feedback comparing the user's answer to that snippet.
    """
    question_embedding = embedder.encode(user_question, convert_to_tensor=True)
    scores = util.cos_sim(question_embedding, doc_embeddings)[0]
    best_idx = scores.argmax()
    best_chunk = doc_chunks[best_idx]

    # Compose a comparative feedback prompt
    prompt = (
        f"Document snippet: {best_chunk}\n\n"
        f"Question: {user_question}\n"
        f"User's Answer: {user_answer}\n\n"
        "Provide constructive feedback on how closely the user's answer matches the content "
        "of the document snippet. Be objective and point out missing or well-covered points."
    )
    # Use summarizer pipeline as lightweight generator
    feedback = summarizer_pipeline(prompt, max_length=120, min_length=50, do_sample=False)[0]['summary_text']

    return feedback, best_chunk
