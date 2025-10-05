from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config import EMBEDDING_MODEL, FAISS_INDEX_PATH

class VectorDBService:

    def __init__(self, embedding_model, index_path):
        self.embeddings = OpenAIEmbeddings(model=embedding_model)
        self.index_path = index_path
        self.knowledge_base = None

    # function to generate knowledge base from existing FAISS kbase
    def load(self):
        self.knowledge_base = FAISS.load_local(self.index_path, self.embeddings, allow_dangerous_deserialization=True)
        print("Loaded FAISS index.")

    # function to regenerate FAISS knowledge base
    def regenerate(self, chunks, metadatas):
        # Takes a list of chunks of text and returns a corresponding list of vector embeddings
        self.knowledge_base = FAISS.from_texts(texts=chunks, embedding=self.embeddings, metadatas=metadatas)
        self.knowledge_base.save_local(self.index_path)
        print("Regenerated FAISS index.")

    # takes embeddings and a query and returns ranked results of most relevant vectors
    def relevant_vectors(self, query):
        results = self.knowledge_base.similarity_search(query)
        for meta in results:
            print(meta.metadata)
        return results