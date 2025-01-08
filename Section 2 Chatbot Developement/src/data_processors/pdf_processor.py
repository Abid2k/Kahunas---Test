import PyPDF2
from typing import List
import os

class PDFProcessor:
    def __init__(self, pdf_directory: str):
        self.pdf_directory = pdf_directory
    
    def extract_workout_instructions(self, program_name: str) -> str:
        pdf_path = os.path.join(self.pdf_directory, f"{program_name}.pdf")
        
        if not os.path.exists(pdf_path):
            return "Program instructions not found."
        
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
        
        return text 