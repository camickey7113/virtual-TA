from service import PDFService, VectorDBService, LLMService

class QAService():

    def question_to_answer(query):
        # file = open("materials/01_CS449_Introduction.pdf")
        chunks = PDFService.extract_chunks("materials/01_CS449_Introduction.pdf")

        vectors = VectorDBService.relevant_vectors(query, chunks)

        response = LLMService.generate_response(query, vectors)

        return response