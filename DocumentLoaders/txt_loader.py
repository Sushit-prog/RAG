from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("human", "Write a summary for the following poem - \n {poem}")
])

loader = TextLoader(r'C:\Users\pakra\Desktop\RAG\DocumentLoaders\cricket.txt', encoding='utf-8')
docs = loader.load()

print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem': docs[0].page_content}))