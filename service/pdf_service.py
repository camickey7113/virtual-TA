from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
import os

class PDFService:
    # Converts a pdf file to chunks
    @staticmethod
    def extract_chunks(file):
        # Convert PDF to text
        reader = PdfReader(file)
        all_text = ""
        for page in reader.pages:
            all_text += page.extract_text()

        # Convert text to chunks
        text_splitter = CharacterTextSplitter(
                    separator="\n",
                    chunk_size=1000,
                    chunk_overlap=200,
        )
        return text_splitter.split_text(all_text)
    
    @staticmethod
    def extract_chunks_from_folder(folder_path):
        all_chunks = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            chunks = PDFService.extract_chunks(file_path)
            all_chunks.extend(chunks)
        return all_chunks