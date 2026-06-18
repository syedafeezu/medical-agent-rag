import streamlit as st

from utils.ingest import load_pdf
from utils.rag_chain import create_db, get_llm

from langchain.chains import RetrievalQA

st.title("🩺 Medical Research Assistant")

pdf = st.file_uploader("Upload PDF")

if pdf:

    with open(pdf.name,"wb") as f:
        f.write(pdf.read())

    chunks = load_pdf(pdf.name)

    db = create_db(chunks)

    qa = RetrievalQA.from_chain_type(
        llm=get_llm(),
        retriever=db.as_retriever()
    )

    question = st.text_input("Ask a question")

    if question:

        answer = qa.run(question)

        st.write(answer)