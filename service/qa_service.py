from service import PDFService, VectorDBService, LLMService
from config import EMBEDDING_MODEL, FAISS_INDEX_PATH, MATERIALS_FOLDER_NAME
import os

class QAService():

    def __init__(self, rebuild):
        # prepare to generate index
        chunks = None
        index_exists = os.path.exists(FAISS_INDEX_PATH)

        self.knowledge_base = VectorDBService(embedding_model=EMBEDDING_MODEL, index_path=FAISS_INDEX_PATH)
        if index_exists and not rebuild:
            self.knowledge_base.load()
        else:
            chunks = PDFService.extract_chunks_from_folder(MATERIALS_FOLDER_NAME)
            self.knowledge_base.regenerate(chunks)

        self.llm_service = LLMService()

    def question_to_answer(self, query):
        vectors = self.knowledge_base.relevant_vectors(query)
        response = self.llm_service.generate_response(query, vectors)
        return response