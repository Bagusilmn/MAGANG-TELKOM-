from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os

def load_popu_chain():
    os.environ["OPENAI_API_KEY"] = "your-api-key"
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local("vector_index_popu/popu_index", embeddings, allow_dangerous_deserialization=True)

    prompt_template = """Halo! Kamu asisten digital Telkomsel...
    {context}
    Pertanyaan: {question}
    Berikan jawaban dari data di atas:"""

    prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)

    llm = ChatOpenAI(
        model_name="meta-llama/llama-4-scout:free",
        openai_api_base="https://openrouter.ai/api/v1"
    )

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 50}),
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
