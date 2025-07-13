import streamlit as st
from backend.document_loader import extract_text_from_file
from backend.summarizer import chunk_text, summarize_text
from backend.qa_module import build_context_index, answer_question
from backend.question_gen import generate_questions
from backend.evaluator import evaluate_answer

st.set_page_config(page_title="Smart Research Assistant", layout="wide")
st.title("📚 Smart Research Assistant (Offline)")
st.write("Upload a PDF or TXT file to get a summary, ask questions, be challenged, and evaluate your answers!")

# Upload
uploaded_file = st.file_uploader("Choose a PDF or TXT file", type=['pdf','txt'])

if uploaded_file:
    # Extract
    text = extract_text_from_file(uploaded_file)
    st.subheader("📝 Extracted Content")
    st.text_area("Document Text", text, height=200)

    # Summarize
    chunks = chunk_text(text, max_length=1000)
    summary = ""
    for chunk in chunks:
        summary += summarize_text(chunk) + " "
    st.subheader("🔍 Summary (≈150 words)")
    st.write(summary)

    # Build embeddings index for Q&A & evaluation
    ctx_chunks, ctx_embeddings = build_context_index(text)

    # Free-form Q&A
    st.header("🤔 Ask Anything")
    user_question = st.text_input("Type your question here:")
    if user_question:
        answer, snippet = answer_question(user_question, ctx_chunks, ctx_embeddings)
        st.success(f"Answer: {answer}")
        with st.expander("See supporting snippet"):
            st.info(snippet)

    # Challenge Mode
    st.header("🎯 Challenge Me")
    if st.button("Generate Challenge Questions"):
        questions = generate_questions(text)
        st.session_state['challenge_questions'] = questions
    # Display questions if generated
    if 'challenge_questions' in st.session_state:
        for idx, q in enumerate(st.session_state['challenge_questions'], start=1):
            st.write(f"**Q{idx}:** {q}")

    # Evaluation
    st.header("📝 Evaluate Your Answer")
    user_q_for_eval = st.text_input("Paste a question (like from challenge) here:")
    user_ans = st.text_area("Type your answer here:")
    if st.button("Evaluate Answer"):
        if user_q_for_eval and user_ans:
            feedback, support_snippet = evaluate_answer(user_q_for_eval, user_ans, ctx_chunks, ctx_embeddings)
            st.success("✅ Feedback on Your Answer")
            st.write(feedback)
            with st.expander("See relevant document snippet"):
                st.info(support_snippet)
        else:
            st.warning("Please provide both a question and your answer.")
