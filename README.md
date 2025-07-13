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

## ✨ Project Highlights

🚀 **Runs fully offline:** No need for OpenAI API keys, billing, or internet beyond the first model download.  
🧩 **Modular design:** Each function is separated into logical modules (`document_loader`, `summarizer`, `qa_module`, `question_gen`, `evaluator`), making it highly maintainable and extensible.  
📝 **Research-focused:** Designed for academic papers and technical documents, but easily adaptable for general documents.  
💡 **Smart logic:** Uses sentence transformers (`all-MiniLM-L6-v2`) for semantic similarity, T5 for question generation, and BART for summarization and feedback — all local.  
🎯 **Streamlit-powered UI:** Instant web interface with no heavy frontend coding.  
⚡ **Deploy-ready:** 1-click deployment on Streamlit Cloud for easy sharing and demonstration.

---

## 📸 Screenshots

| Upload Document | Ask Anything | 
|-----------------|--------------|------------------------|
| ![upload](upload.png) | ![qa](qa.png) |


## 🎥 Demo

[![Watch the demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://youtu.be/OapPrLIMpPk)

📺 Click the image above to watch a full walkthrough of the Smart Research Assistant in action.

### 📌 Clone the repo
```bash
git clone https://github.com/yourusername/smart-research-assistant.git
cd smart-research-assistant

```
---

🚀 Thank you for exploring the Smart Research Assistant!  
I hope this project inspires you to push the boundaries of what's possible with NLP and local AI applications.

If you have suggestions, questions, or just want to connect, feel free to reach out.  
Let's build smarter tools together! 💡

