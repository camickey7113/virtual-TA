from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
import os

class PDFService:
    # Converts a pdf file to chunks
    @staticmethod
    def extract_chunks(file):
        # Convert PDF to text
        reader = PdfReader(file)
        # all_text = ""
        # for page in reader.pages:
        #     all_text += page.extract_text()

        # Convert text to chunks
        text_splitter = CharacterTextSplitter(
                    separator="\n",
                    chunk_size=1000,
                    chunk_overlap=200,
        )

        chunks = []
        metadatas = []

        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            if not text:
                continue

            page_chunks = text_splitter.split_text(text)
            chunks.extend(page_chunks)

            metadatas.extend([
                {
                    "source": os.path.basename(file),
                    "page": page_num + 1
                }
                for _ in page_chunks
            ])

        return chunks, metadatas
    
    @staticmethod
    def extract_chunks_from_folder(folder_path):
        all_chunks = []
        all_metadatas = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            chunks, metadatas = PDFService.extract_chunks(file_path)
            all_chunks.extend(chunks)
            all_metadatas.extend(metadatas)
        return all_chunks, all_metadatas