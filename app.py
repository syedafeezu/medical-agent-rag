import streamlit as st

from utils.ingest import load_pdf
from utils.rag_chain import create_db, get_llm

st.title("🩺 Medical Research Assistant")

pdf = st.file_uploader("Upload PDF", type="pdf")

if pdf:

    with open(pdf.name, "wb") as f:
        f.write(pdf.read())

    chunks = load_pdf(pdf.name)

    db = create_db(chunks)

    retriever = db.as_retriever()

    question = st.text_input("Ask a question")

    if question:

        docs = retriever.invoke(question)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""

        llm = get_llm()

        response = llm.invoke(prompt)

        st.subheader("Answer")

        st.write(response.content)