# AI PDF Q&A Assistant

Upload any PDF and ask questions about it — powered by Claude API.

## What this project does
- User PDF upload karta hai (resume, notes, report, kuch bhi)
- App PDF se text nikalta hai
- User question poochta hai us document ke baare mein
- Claude API document padh kar answer deta hai

## Tech Stack
- **Python** — core language
- **Streamlit** — web UI (bina HTML/CSS ke web app banane ke liye)
- **pypdf** — PDF se text extract karne ke liye
- **Anthropic API (Claude)** — question answering ke liye (LLM)

## How to run this locally

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   streamlit run app.py
   ```

3. Browser mein app khul jayega (usually http://localhost:8501)

4. Sidebar mein apni Anthropic API key daalo (free key yaha se milti hai: https://console.anthropic.com/)

5. PDF upload karo aur question poocho!

## How to explain this in an interview

Yeh project bolo ki:
- "Maine ek document Q&A tool banaya hai jo PDF se text extract karke, LLM (Claude API) ko context ke saath prompt bhejta hai, aur relevant answer return karta hai."
- "Streamlit use kiya UI ke liye kyunki fast prototyping ke liye best hai."
- "Prompt engineering ka concept use kiya — document ka content system prompt mein inject karke model ko batata hoon ki sirf usi document se answer de."
- Agar poochein "isko improve kaise karoge?" — bolo: "Bade documents ke liye main RAG (Retrieval Augmented Generation) add kar sakta hoon — chunking + embeddings + vector database (jaise FAISS ya Pinecone), taaki poora document ek saath API mein na bhejna pade."

Yeh answer dikhata hai ki tumhe basic implementation ke saath-saath advanced concept (RAG) ka bhi pata hai — even agar tumne implement nahi kiya, mention karna smart lagta hai.

## Next steps (optional, agar time mile)
- Isko free deploy karo Streamlit Community Cloud pe (free hai, 10 min lagte hain) — taaki live link resume mein daal sako
- GitHub pe push karo with a good README (jaisa yeh hai)
- LinkedIn pe short demo video/GIF post karo

## Resume mein kaise likhen
> Built an AI-powered PDF Q&A application using Python, Streamlit, and Claude API that extracts document content and answers user queries via LLM-based question answering, demonstrating practical application of prompt engineering and API integration.