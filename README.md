# iDoc-RAG: AI-Powered Document Intelligence

![Project Banner](docs/banner.png)  
*A smart document Q&A system powered by Llama3 and RAG architecture*

## 🌟 Features
- **Multi-Format Support**: Process PDFs, Word docs, and text files  
- **Smart Chunking**: Dynamic text splitting optimized for document complexity  
- **Hybrid Search**: Vector + keyword retrieval for better accuracy  
- **Persistent Storage**: ChromaDB/Supabase integration options  
- **Deployment-Ready**: Pre-configured for Vercel/Streamlit Sharing  

## 🛠️ Tech Stack
| Component          | Technology                  |
|--------------------|-----------------------------|
| LLM                | Llama3-70B (Groq API)       |
| Embeddings         | BAAI/bge-small-en-v1.5      |
| Vector Store       | FAISS/ChromaDB              |
| Framework          | LangChain                   |
| UI                 | Streamlit                   |

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- [Groq API key](https://console.groq.com/keys)
- (Optional) [Supabase account](https://supabase.com)

# Install dependencies
pip install -r requirements.txt
