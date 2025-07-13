# 📚 Smart Research Assistant (Offline AI App)

[![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://smart-research-assistant-anuragt092.streamlit.app)
An AI-powered offline research assistant built with **Streamlit** and **Hugging Face Transformers**.  
Upload PDF/TXT documents and the assistant will:

✅ Automatically summarize your documents  
✅ Let you ask free-form questions about them  
✅ Generate logical comprehension-style questions  
✅ Evaluate your answers with constructive feedback  

Runs fully **offline** on your machine — no OpenAI API keys needed, no quota limits.

---

## 🚀 Features

- 📄 **Upload PDF/TXT**: Parses research papers, articles, or notes.
- ✍️ **Summarization**: Generates concise summaries (~150 words) using `facebook/bart-large-cnn`.
- 🤔 **Ask Anything**: Ask natural questions and get smart answers based on document context.
- 🎯 **Challenge Me**: Automatically generates comprehension questions to test your understanding.
- ✅ **Evaluate Answers**: Grades your answers with meaningful feedback using semantic similarity.

---

## ⚡ Quick Start

### 📌 Clone the repo
```bash
git clone https://github.com/yourusername/smart-research-assistant.git
cd smart-research-assistant
