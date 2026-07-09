#  AI PDF Q&A Assistant

An AI-powered web app that lets users upload any PDF document and ask natural-language questions about its content. Built with Python, Streamlit, and the Groq API (Llama 3.3 70B).

Live Demo: https://ai-pdf-q-a-project-jns2ftgmzjxzshzfldqiv6.streamlit.app/

## Features

- Upload any PDF and extract its text content automatically
- Ask natural-language questions about the document
- Get accurate, context-grounded answers powered by an LLM (Llama 3.3 70B via Groq)
- Clean, simple UI built with Streamlit — no frontend code required
- Fast inference thanks to Groq's LPU-based API

## Tech Stack

Component,Technology
🐍 Language,Python
🎈 Web UI,Streamlit
📄 PDF Parsing,pypdf
🧠 LLM Provider,Groq API (LLaMA 3.3 70B)
☁️ Deployment,Streamlit Community Cloud


##  How It Works

1. User uploads a PDF file through the Streamlit interface
2. The app extracts raw text from the PDF using `pypdf`
3. When the user asks a question, the extracted text + question are sent as a prompt to the Groq API
4. The LLM generates an answer grounded strictly in the document content
5. The answer is displayed back to the user in real time

## Installation & Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your Groq API key. Create a file at `.streamlit/secrets.toml` with:
   ```toml
   GROQ_API_KEY = "your_api_key_here"
   ```
   Get a free API key at [console.groq.com/keys](https://console.groq.com/keys).

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open the local URL shown in the terminal (usually `http://localhost:8501`).

##  Deployment

This app is deployed on **Streamlit Community Cloud**. To deploy your own copy:

1. Push this repo to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click "New app", select this repo and `app.py` as the entry point
4. Under "Advanced settings → Secrets", add:
   ```toml
   GROQ_API_KEY = "your_api_key_here"
   ```
5. Click Deploy

## Future Improvements

- Add RAG (Retrieval-Augmented Generation) with vector embeddings for handling larger documents efficiently
- Support multiple PDF uploads and cross-document search
- Add conversation history / follow-up question support
- Support additional file formats (DOCX, TXT)

## License

This project is open source and available under the MIT License.

---

*Built as a learning project to explore LLM API integration and prompt engineering.*
