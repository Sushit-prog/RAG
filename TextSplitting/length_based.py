from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r'C:\Users\pakra\Desktop\RAG\TextSplitting\week 5Resolution-Refutatiom.pdf')

docs = loader.load()


splitter = CharacterTextSplitter(
  chunk_size = 500,
  chunk_overlap = 0,
  separator=''
)

result = splitter.split_documents(docs)
print(result[3].page_content)