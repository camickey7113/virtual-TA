from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

class VectorDBService:

    def relevant_vectors(query, chunks):
        # Takes a list of chunks of text and returns a corresponding list of vector embeddings
        embeddings = OpenAIEmbeddings()
        db = FAISS.from_texts(chunks, embeddings)

        # Takes embeddings and a query and returns ranked results of most relevant vectors
        relevant_vectors = db.similarity_search(query)
        return relevant_vectors