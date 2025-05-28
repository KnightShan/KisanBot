# 🌾 KISANCHAT — An AI Chatbot for Indian Farmers

KISANCHAT is an AI-powered chatbot designed to assist Indian farmers with agricultural queries. It uses retrieval-augmented generation (RAG) over local documents to provide accurate, informative, and context-aware answers in a conversational interface.

---

## 🧠 Features

- 📚 **Document-based Q&A** — Chatbot retrieves and answers from agricultural PDFs.
- 🤖 **LLM Integration** — Uses Together.ai's Mistral-7B-Instruct for intelligent responses.
- 🔍 **Semantic Search** — Pinecone-powered vector search with HuggingFace embeddings.
- 🧾 **ChatGPT-like UI** — Modern web interface built using Flask.
- 🧠 **RAG Chain** — Combines document retrieval with generative response for accurate results.

---

## ⚙️ Tech Stack

| Layer            | Technology                        |
|------------------|------------------------------------|
| Backend          | Python, Flask                      |
| LLM              | Together.ai (Mistral-7B-Instruct)  |
| Vector DB        | Pinecone                           |
| Embeddings       | HuggingFace (MiniLM-L6-v2)         |
| PDF Processing   | LangChain                          |
| UI               | HTML, CSS                          |

---

## 🏁 Getting Started

### 🔧 Prerequisites

- Python 3.9+
- `pip install -r requirements.txt`
- Pinecone API key
- Together.ai API key

### 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/KnightShan/kisanchat.git
   cd kisanchat

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set your environment variables**  
   Add a .env file or set in your code:
   ```ini
   PINECONE_API_KEY=your-pinecone-key
   TOGETHER_API_KEY=your-together-key

4. **Add your PDF files**  
   Place them in the Data/ folder.

5. **Run the index creation script**
   ```bash
   python store_index.py

6. **Start the Flask app**
   ```bash
   python app.py

7. **Open in browser**  
   Visit: http://localhost:8080

