import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

DATA_PATH = "Data"
VECTOR_DB_PATH = "vectorstore"


def ingest_documents():
    documents = []

    # Load PDF files
    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            file_path = os.path.join(DATA_PATH, file)
            loader = PyPDFLoader(file_path)
            documents.extend(loader.load())

    print(f"Loaded {len(documents)} pages")

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    # FREE local embeddings (no API key required)
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    # Store embeddings in FAISS
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTOR_DB_PATH)

    print(" Vector store created successfully")


if __name__ == "__main__":
    ingest_documents()
