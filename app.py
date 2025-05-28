from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_together import Together
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import *
import os

app = Flask(__name__)

os.environ["PINECONE_API_KEY"] = "pcsk_2wd5Md_7PxVMMgDW3dFaAUWdEKYXgcLg6jkzWZVtwaZPG7G8ZqkcMEYiicFCSrugzo2YY4"
os.environ["TOGETHER_API_KEY"] = "ef850308ffbd20d15cf5d3d62bd083060d9669cfdde42b02ba06bc4edd7fdb16"

embeddings = download_hugging_face_embeddings()

index_name = "agribot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

llm = Together(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    temperature=0.4,
    max_tokens=500
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    response = rag_chain.invoke({"input": msg})
    return str(response["answer"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)  
