from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class LLMService():
    
    def __init__(self, model_name="gpt-4", temperature=0):
        self.llm = ChatOpenAI(model_name=model_name, temperature=temperature)
        self.prompt_template = ChatPromptTemplate.from_template("""
            You are a knowledgeable assistant. You can only answer questions using the context provided below.
            If the answer is not in the context, say "I wasn't able to find the answer to that in the notes...".

            Context:
            {context}

            Question:
            {question}

            Answer:
        """)
        self.chain = create_stuff_documents_chain(self.llm, self.prompt_template)

    def generate_response(self, query, relevant_vectors):
        # Set up llm model
        answer = self.chain.invoke({
            "context":relevant_vectors,
            "question":query
        })
        return answer
