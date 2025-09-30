from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter

class PDFService:
    # Converts a pdf file to chunks
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

    

    
