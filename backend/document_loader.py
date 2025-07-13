# backend/document_loader.py

import fitz  # PyMuPDF

def extract_text_from_file(uploaded_file):
    """
    Extract text from an uploaded PDF or TXT file.
    """
    if uploaded_file.type == "application/pdf":
        pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf:
            text += page.get_text()
        return text
    else:
        # Assume text file
        return uploaded_file.read().decode("utf-8")
