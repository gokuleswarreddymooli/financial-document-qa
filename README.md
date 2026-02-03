# 📊 Financial Document Q&A System (RAG)

A Retrieval-Augmented Generation (RAG) based application that allows users to ask natural-language questions about large financial documents such as SEC 10-K reports and receive accurate, source-grounded answers.

---

## 🚀 Project Overview

Financial documents are often hundreds of pages long, making it difficult and time-consuming to extract relevant information.  
This project solves that problem by combining semantic search and question answering to enable interactive exploration of financial documents.

The system:
- Ingests large PDF documents (SEC 10-K)
- Converts text into vector embeddings
- Retrieves relevant document sections using semantic similarity
- Answers questions strictly based on retrieved content
- Displays answers along with source references

---

## 🧠 Key Concepts Used

- Retrieval-Augmented Generation (RAG)
- Vector Embeddings
- Semantic Search
- FAISS Vector Database
- Extractive Question Answering
- Streamlit Web Application

---

## 🏗️ System Architecture

PDF (10-K Report)
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
FAISS Vector Store
↓
User Question
↓
Semantic Retrieval
↓
Question Answering Model
↓
Answer + Source Documents


---

## 📂 Project Structure



Financial rag project/
├── Data/
│ └── 10-K-2025-As-Filed.pdf
├── ingest.py
├── rag_pipeline.py
├── app.py
├── vectorstore/
└── README.md


---

## ⚙️ How the Project Works

### 1️⃣ Document Ingestion
- Loads SEC 10-K PDF documents
- Splits text into overlapping chunks
- Converts chunks into vector embeddings
- Stores embeddings in a FAISS vector database

### 2️⃣ Retrieval & Question Answering
- Converts user questions into embeddings
- Retrieves the most relevant document chunks using FAISS
- Uses an extractive QA model to generate answers strictly from the retrieved context

### 3️⃣ User Interface
- Built using Streamlit
- Users can enter questions
- Displays answers and source documents
- Includes loading indicators and error handling

---

## 🧪 Example Questions

- What is the company’s business overview?
- What are the main revenue sources?
- What major risk factors are mentioned?
- What products or services does the company offer?

---

## 🖥️ Running the Application Locally

### 1️⃣ Create virtual environment

python -m venv venv
venv\Scripts\Activate   # Windows

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run document ingestion
python ingest.py

4️⃣ Launch the Streamlit app
streamlit run app.py

🛠️ Technologies Used

Python

LangChain

FAISS

HuggingFace Transformers

Sentence-Transformers

Streamlit

🎯 Why Retrieval-Augmented Generation?

Prevents hallucination by grounding answers in documents

Scales to large documents beyond LLM context limits

Allows easy document updates without retraining models

Improves reliability for financial and factual data

📈 Future Improvements

Support for multiple PDF documents

Page-level citations

Answer summarization mode

Cloud deployment (AWS / GCP)

Replace local models with hosted LLMs

📌 Resume Summary

Built an end-to-end Retrieval-Augmented Generation (RAG) system to enable semantic question answering over SEC 10-K financial documents using LangChain, FAISS, and HuggingFace models. Implemented document ingestion, vector embeddings, semantic retrieval, and an interactive Streamlit interface to generate accurate, source-backed answers.

📜 License

This project is for educational and demonstration purposes.
