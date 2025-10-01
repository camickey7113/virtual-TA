from service import PDFService, VectorDBService, LLMService
from config import EMBEDDING_MODEL, FAISS_INDEX_PATH
import os

class QAService():

    def __init__(self):
        # set up knowledge base
        # declare folder where class materials are stored
        materials_folder = "materials"

        # prepare to generate index
        chunks = None
        index_exists = os.path.exists(FAISS_INDEX_PATH)

        self.knowledge_base = VectorDBService(embedding_model=EMBEDDING_MODEL, index_path=FAISS_INDEX_PATH)
        if index_exists:
            self.knowledge_base.load()
        else:
            chunks = PDFService.extract_chunks("materials/01_CS449_Introduction.pdf")
            self.knowledge_base.regenerate(chunks)

        self.llm_service = LLMService()

    def question_to_answer(self, query):
        vectors = self.knowledge_base.relevant_vectors(query)
        response = self.llm_service.generate_response(query, vectors)
        return response