# iDoc: RAG based chatbot for your documents 

*powered by Llama3*

## Features
- **Multi-Format Support**: Process PDFs, Word docs, and text files  
- **Smart Chunking**: Dynamic text splitting optimized for document complexity  
- **Modular Design**: Replace any component with minimal changes to codebase   

## Tech Stack
| Component          | Technology                  |
|--------------------|-----------------------------|
| LLM                | Llama3-70B (Groq API)       |
| Embeddings         | all-MiniLM-L6-v2            |
| Vector Store       | FAISS                       |
| Framework          | LangChain                   |
| UI                 | Streamlit                   |

## Quick Start
- Clone this repository or download it locally
- Run : streamlit run app.py (inside the project folder)

### Prerequisites
- Python 3.10+
- [Groq API key](https://console.groq.com)

# Install dependencies
pip install -r requirements.txt
