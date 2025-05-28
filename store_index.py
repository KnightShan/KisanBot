from src.helper import load_pdf_file, text_split, download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import os

extracted_data=load_pdf_file(data='Data/')

text_chunks=text_split(extracted_data)
embeddings = download_hugging_face_embeddings()

pc = Pinecone(api_key="pcsk_2wd5Md_7PxVMMgDW3dFaAUWdEKYXgcLg6jkzWZVtwaZPG7G8ZqkcMEYiicFCSrugzo2YY4")  
index_name = "agribot"

if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  
        metric="cosine",  
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )


os.environ["PINECONE_API_KEY"] = "pcsk_2wd5Md_7PxVMMgDW3dFaAUWdEKYXgcLg6jkzWZVtwaZPG7G8ZqkcMEYiicFCSrugzo2YY4"

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings
)

