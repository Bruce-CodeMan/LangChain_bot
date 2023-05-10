'''
Date: 2023-05-10 15:15:23
Author: Bruce
Description: Added to Pinecone VectorStore vectors
'''

from decouple import config
from langchain.document_loaders import ReadTheDocsLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
import pinecone

# Import Custom Functions
import config.constants as constants

pinecone.init(
    api_key=config("PINECONE_API_KEY"),
    environment=config("PINECONE_ENVIRONMENT_REGION")
)

def ingest_docs():
    loader = ReadTheDocsLoader(path="./docs")
    raw_documents = loader.load()
    # print(f"loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50, separators=["\n\n", "\n", " ", ""])
    documents = text_splitter.split_documents(documents=raw_documents)
    # print(len(documents))
    # print(documents[1])

    for doc in documents:
        old_path = doc.metadata["source"]
        new_url = old_path.replace("docs/langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})
    
    print(f"Going to insert {len(documents)} to Pinecone")
    embeddings = OpenAIEmbeddings(openai_api_key=config("OPENAI_API_KEY"))
    Pinecone.from_documents(documents=documents, embedding=embeddings, index_name=constants.INDEX_NAME)
    print("Added to Pinecone vectorStore vectors")

if __name__ == '__main__':
    ingest_docs()