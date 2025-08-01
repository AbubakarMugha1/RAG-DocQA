# iDoc: Instant Document QA with RAG  
*Powered by Llama3 & optimized for speed*

![Demo Screenshot](assets/screenshot1.png) *(Add your screenshot here)*

## 🚀 Features  
- **Instant Search**: Binary embeddings deliver fast retrieval with minimal accuracy loss  
- **Multi-Format Support**:  
  📄 PDFs  
  📝 Word (.docx)  
  📋 Plain text (.txt)  
- **Self-Contained**: ChromaDB stores vectors locally  
- **Smart Processing**: Dynamic chunking adapts to document complexity  

## 🛠️ Tech Stack  

| Component       | Technology                  |  
|-----------------|-----------------------------|  
| LLM             | Llama3-70B (Groq API)       |  
| Embeddings      | BGE-small (binary mode)     |  
| Vector Store    | ChromaDB                    |  
| Framework       | LangChain                   |  
| UI              | Streamlit                   |  

## ⚡ Quick Start

### Prerequisites
- Python 3.10+
- [Groq API key](https://console.groq.com)

### Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/iDoc.git
   cd iDoc
