from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langserve import add_routes
import uvicorn
import os
from langchain_community.document_loaders import CSVLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.globals import set_debug

load_dotenv()
set_debug(True)

openai_api_key = os.environ["OPENAI_API_KEY"]

app = FastAPI(
    title="Python Assistent",
    version="1.0",
    decsription="API Server"
)
model = ChatOpenAI(api_key=openai_api_key, temperature=0, streaming=True, model="gpt-4o")


loader = CSVLoader("content.csv")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

retriever = db.as_retriever()

chain = ConversationalRetrievalChain.from_llm(model, retriever)

add_routes(
    app,
    chain,
    path="/chat"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)