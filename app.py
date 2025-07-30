import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader #for PDFs
from docx import Document #for Word documents
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS #Facebook AI Similarity Search
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq

#-----Text Extraction Functions------#
def extract_from_PDF(pdf): #function to extract text from PDF's
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    return text

def extract_from_Word(file): #function to extract text from Word Documents
    word_file = Document(file)
    text = "\n".join([paragraph.text for paragraph in word_file.paragraphs])
    
    return text

def extract_from_txt(file): #function to read from plain text files (notepad etc.)
    return file.read().decode('utf-8')


#------Dynamic Chunk Size Calculation/Text Splitting------#
def make_chunks(text):
    #determining ideal chunk size based on the input document. Base value established between 500-1500
    doc_length = len(text)
    base_size = min(max(int(doc_length * 0.01), 500), 1500) #500-1500 dependent on document length
    #assumption here is that longer documents (like research papers should have larger context windows compared to 
    #smaller documents like a conversation)

    #scaling chunk size according to word density
    words = text.split()
    avg_word_length = 0
    if words:
        avg_word_length = ((sum(len(w) for w in words)) / len(words)) #avg word length calculation
    else:
        avg_word_length = 5.0

    density_factor = max(1.0, avg_word_length / 5.0) #scaling chunk size according to word density of document
    chunk_size = int(base_size / density_factor)
    chunk_overlap = min(max(100, int(0.2 * chunk_size)), chunk_size // 2) 

    splitter = RecursiveCharacterTextSplitter( 
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        separators = ["\n\n", "\n", " ", ""]
    )

    return splitter.split_text(text)

def main():
    load_dotenv()
    #webpage design
    st.set_page_config(page_title = "iDoc")
    st.header("iDoc - Powered by Llama3 70B")

    #upload files
    files = st.file_uploader(label = "Upload Documents:", type = ["pdf", "docx", "txt"], label_visibility = "hidden", accept_multiple_files = True)

    #check if valid file
    if files:
        #determine document type and then extract text accordingly
        valid_files = 0
        all_chunks = []
        for file in files:
            text = ""
            if file.type == "application/pdf": #for PDF
                text = extract_from_PDF(file)
                # st.write(text)

            elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document": #for Word files
                text = extract_from_Word(file)
                # st.write(text)
            
            elif file.type == "text/plain": #for notepad etc.
                text = extract_from_txt(file)
                # st.write(text)

            else:
                st.error("Invalid file type entered!")
                continue

            #split extracted text into chunks
            chunks = make_chunks(text)
            if chunks:
                all_chunks.extend(chunks)
                valid_files += 1
                st.success(f"Document was successfully split into {len(chunks)} chunks!")

            #creating embeddings

        if len(all_chunks) > 0 and valid_files > 0: #if any chunks were made/files were processed
            embeddings = HuggingFaceBgeEmbeddings(model_name = "all-MiniLM-L6-v2", model_kwargs={"device": "cpu"})
            knowledge_base = FAISS.from_texts(all_chunks, embeddings) #set up local knowledge base

            query = st.text_input("Ask a question about your documents:") 
            
            llm = ChatGroq(model_name = "llama3-70b-8192", #set up LLM 
                    api_key = os.getenv("GROQ_API_KEY"),
                    temperature = 0.4) 
            
            if query:
                with st.spinner("Searching your documents 🚀"):

                    qa_chain = RetrievalQA.from_chain_type(
                        llm = llm,
                        chain_type = "stuff",
                        retriever = knowledge_base.as_retriever()
                    )

                    response = qa_chain.run(query)
                    st.write(response)  
        else:
            st.error("No valid chunks were generated from uploaded file(s)")

if __name__ == '__main__':
    main()