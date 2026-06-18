from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.vectorstores import Chroma

def create_db(chunks):

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    db = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="chroma_db"
    )

    return db


def get_llm():

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.2
    )