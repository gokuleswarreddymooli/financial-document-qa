import streamlit as st
from rag_pipeline import load_qa_chain
import os

# Page configuration
st.set_page_config(
    page_title="Financial Document Q&A",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.title("📊 Financial Q&A System")
st.sidebar.markdown(
    """
    **What does this app do?**  
    This system allows you to ask natural-language questions about large
    financial documents (SEC 10-K reports).

    **How it works:**
    - Documents are embedded into a vector database
    - Relevant sections are retrieved using semantic search
    - Answers are extracted directly from the source

    **Technology:**
    - FAISS
    - HuggingFace Models
    - Streamlit
    """
)

st.sidebar.markdown("---")
st.sidebar.write("Built as a Retrieval-Augmented Generation (RAG) project.")

# Main title
st.title("📈 Financial Document Question & Answer System")
st.write("Ask questions about the SEC 10-K document and get source-backed answers.")

# Safety check
if not os.path.exists("vectorstore"):
    st.error("Vector store not found. Please run ingest.py first.")
    st.stop()

# Load QA pipeline
with st.spinner("Loading AI system..."):
    qa_fn = load_qa_chain()

# Question input
question = st.text_input(
    "🔍 Enter your question:",
    placeholder="e.g. What are the main revenue sources?"
)

if question:
    with st.spinner("Searching document and generating answer..."):
        response = qa_fn(question)

    st.markdown("### ✅ Answer")
    st.success(response["result"])

    st.markdown("### 📄 Source Documents")
    for i, doc in enumerate(response["source_documents"], start=1):
        with st.expander(f"Source {i}"):
            st.write(doc.page_content[:1000] + "...")
            st.caption(doc.metadata.get("source", "Unknown source"))
