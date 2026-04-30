from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

loader = PyPDFLoader(r'C:\Users\pakra\Desktop\RAG\DocumentLoaders\week 5Resolution-Refutatiom.pdf')

docs = loader.lazy_load()

                               
for document in docs:
  print(document.metadata)