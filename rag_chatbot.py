import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import ChatOllama
import os
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.storage import LocalFileStore
from langchain.embeddings import CacheBackedEmbeddings
import openai
from dotenv import load_dotenv
client = openai.OpenAI()
load_dotenv(verbose=True)
api_key = os.getenv("OPENAI_API_KEY")



if os.path.isdir("./mycache") == False:
    os.mkdir("./mycache")


if os.path.isdir("./mycache/files") == False:
    os.mkdir("./mycache/files")
   
if os.path.isdir("./mycache/embedding") == False:
    os.mkdir("./mycache/embedding")
   
store = LocalFileStore("./mycache/embedding")




st.title("RAG 기반 챗봇")


with st.sidebar:
    uploaded_file = st.file_uploader("파일 업로드", type=['pdf'])




def processing(file):
    file_contents = file.read()
    #파일 저장
    with open(f"./mycache/files/{file.name}", "wb") as f:
        f.write(file_contents)


    #파일 임베딩
    # insert your code
    loader = PDFPlumberLoader(f"./mycache/files/{file.name}")
    docs = loader.load()
    text_spliter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    split_documents = text_spliter.split_documents(docs)
    embeddings = OpenAIEmbeddings()
   
    cached_embedder = CacheBackedEmbeddings.from_bytes_store(
                        underlying_embeddings=embeddings, # 기본 임베딩 모델 지정
                        document_embedding_cache=store # 로컬 저장소 지정
                    )
    vectorstore = FAISS.from_documents(documents=split_documents, embedding=cached_embedder)
    retriever = vectorstore.as_retriever()


    #######
    return retriever


if uploaded_file:
    retriever = processing(uploaded_file)