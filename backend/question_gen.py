# backend/question_gen.py

from transformers import pipeline

# Load simpler model
qg_pipeline = pipeline("text2text-generation", model="t5-small")

def generate_questions(text, num_questions=3):
    chunks = []
    while text:
        if len(text) <= 300:
            chunks.append(text)
            break
        split_pos = text.rfind('. ', 0, 300)
        if split_pos == -1:
            split_pos = 300
        else:
            split_pos += 1
        chunks.append(text[:split_pos])
        text = text[split_pos:].lstrip()

    questions = []
    for chunk in chunks:
        if len(questions) >= num_questions:
            break
        prompt = f"generate three comprehension questions from: {chunk}"
        result = qg_pipeline(prompt, max_length=64)[0]['generated_text']
        questions.append(result)
    return questions
