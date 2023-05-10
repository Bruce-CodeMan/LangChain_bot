'''
Date: 2023-05-10 15:17:28
Author: Bruce
Description: backend api
'''
import os
from typing import Any
import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
from decouple import config


pinecone.init(
    api_key=config("PINECONE_API_KEY"),
    environment=config("PINECONE_ENVIRONMENT_REGION")
)

os.environ["OPENAI_API_KEY"] = "BruceHsu"

def run_llm(query: str) -> Any:
    embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    doc_search = Pinecone.from_existing_index(index_name="langchain-docs-index", embedding=embeddings)
    chat = ChatOpenAI(verbose=True, temperature=0)
    qa = RetrievalQA.from_chain_type(llm=chat, chain_type="stuff", retriever=doc_search.as_retriever(), return_source_documents=True)
    return qa({"query": query})

if __name__ == '__main__':
    print(run_llm(query="What is langChain?"))