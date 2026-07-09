import streamlit as st
from pypdf import PdfReader
from groq import Groq

st.set_page_config(page_title="AI PDF Q&A Assistant", page_icon="📄")
st.title("📄 AI PDF Q&A Assistant")
st.write("Upload a PDF and ask questions about it. Powered by Groq API (Llama).")


st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key", type="password")
st.sidebar.markdown("[Get a free API key here](https://console.groq.com/keys)")


def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

def ask_groq(api_key, document_text, question):
    client = Groq(api_key=api_key)

    prompt = f"""You are a helpful assistant. Answer the question using ONLY the
information in the document below. If the answer is not in the document, say so.

DOCUMENT:
{document_text[:8000]}

QUESTION: {question}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Reading PDF..."):
        document_text = extract_text_from_pdf(uploaded_file)

    st.success(f"PDF loaded successfully! ({len(document_text)} characters extracted)")

    with st.expander("Preview extracted text"):
        st.write(document_text[:1000] + "...")

    question = st.text_input("Ask a question about this document:")

    if st.button("Get Answer"):
        if not api_key:
            st.error("Please enter your Groq API key in the sidebar.")
        elif not question:
            st.warning("Please type a question first.")
        else:
            with st.spinner("Thinking..."):
                try:
                    answer = ask_groq(api_key, document_text, question)
                    st.markdown("### Answer")
                    st.write(answer)
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    st.info("Upload a PDF to get started.")
