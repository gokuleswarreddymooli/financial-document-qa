from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline

VECTOR_DB_PATH = "vectorstore"


def load_qa_chain():
    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    qa_model = pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad"
    )

    def answer_question(question: str):
        # ✅ NEW API
        docs = retriever.invoke(question)

        context = " ".join([doc.page_content for doc in docs])

        result = qa_model(
            question=question,
            context=context
        )

        return {
            "result": result["answer"],
            "source_documents": docs
        }

    return answer_question
