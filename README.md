# 🩺 Medical Research Assistant (RAG)

An LLM-powered medical document assistant that enables users to upload medical PDFs and ask natural language questions using Retrieval-Augmented Generation (RAG).

Built with LangChain, Gemini, ChromaDB, and Streamlit.

---

## 🚀 Features

* 📄 PDF document ingestion
* ✂️ Intelligent text chunking
* 🔍 Semantic search using vector embeddings
* 🧠 Retrieval-Augmented Generation (RAG)
* 💬 Context-aware question answering
* ⚡ Gemini 2.5 Flash integration
* 🗂 Persistent vector database with ChromaDB
* 🌐 Interactive Streamlit interface

---

## 🛠 Tech Stack

* Python
* LangChain
* Google Gemini API
* ChromaDB
* Streamlit
* PyPDF
* dotenv

---

## 📂 Project Structure

```
medical-agent-rag/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
├── chroma_db/
├── documents/
├── utils/
│   ├── ingest.py
│   └── rag_chain.py
│
├── assets/
│   └── screenshot.png
│
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/medical-agent-rag.git
cd medical-agent-rag
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Generate API key from:

https://aistudio.google.com/app/apikey

---

## ▶️ Running

```bash
streamlit run app.py
```

---

## Example Workflow

1. Upload medical PDF.
2. Documents are chunked and embedded.
3. ChromaDB stores vector embeddings.
4. User asks questions.
5. Relevant context is retrieved.
6. Gemini generates answers based on retrieved information.

---

## Future Enhancements

* Multi-agent workflow
* Citation generation
* Medical summarization agent
* Evaluation framework
* Planner and validator agents
* Support for multiple documents
* Conversation memory

---

## License

MIT License
