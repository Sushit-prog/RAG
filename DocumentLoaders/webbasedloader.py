from langchain_community.document_loaders import WebBaseLoader
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



prompt = ChatPromptTemplate.from_template(
   "Answer the following question \n {question} from the following text \n {text}"
)

parser = StrOutputParser()

url = 'https://docs.langchain.com/oss/python/integrations/embeddings'
loader = WebBaseLoader(url)

doc = loader.load()


chain = prompt | model | parser

print(chain.invoke({'question': 'What does vectorization signifies here?', 'text': doc[0].page_content}))