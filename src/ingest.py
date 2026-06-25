from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("Loading document...")

loader = TextLoader("data/beekeeping.txt")
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20
)

docs = text_splitter.split_documents(documents)

print(f"Chunks Created: {len(docs)}")

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    docs,
    embedding_model
)

vectorstore.save_local("faiss_index")

print("FAISS index saved successfully!")