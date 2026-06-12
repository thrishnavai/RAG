from abc import ABC, abstractmethod
from typing import Optional, Any
from langchain_community.document_loaders import (
    GoogleDriveLoader,
    PyPDFLoader, 
    PyMuPDFLoader,
    TextLoader,
    UnstructuredCSVLoader,
    UnstructuredMarkdownLoader,
    UnstructuredPDFLoader )

class Loader(ABC):
    def __init__(self):
        pass

    @abstractmethod    
    def google_drive_loader(self, filepath:str, *args, **kwargs):
        pass
    
    @abstractmethod    
    def text_loader(self, filepath:str, *args, **kwargs):
        pass

    @abstractmethod    
    def pdf_loader(self, filepath:str, *args, **kwargs):
        pass

    @abstractmethod    
    def pymupdf_loader(self, filepath:str, *args, **kwargs):
        pass

    @abstractmethod    
    def csv_loader(self, filepath:str, *args, **kwargs):
        pass

    @abstractmethod    
    def markdown_loader(self, filepath:str, *args, **kwargs):
        pass

    @abstractmethod    
    def unstructured_pdf_loader(self, filepath:str, *args, **kwargs):
        pass


class DocumentLoader(Loader):
    
    def __init__(self):
        super().__init__()
        pass
    
    def google_drive_loader(self, filepath:str, *args, **kwargs):
        return self.google_drive_loader(filepath)

    def text_loader(self, filepath, *args, **kwargs):
        return TextLoader(filepath, autodetect_encoding=True)
    
    def pdf_loader(self, filepath, *args, **kwargs):
        return PyPDFLoader(filepath)

    def pymupdf_loader(self, filepath, *args, **kwargs):
        return PyMuPDFLoader(filepath)

    def csv_loader(self, filepath, *args, **kwargs):
        return UnstructuredCSVLoader(filepath)

    def markdown_loader(self, filepath, *args, **kwargs):
        return UnstructuredMarkdownLoader(filepath)

    def unstructured_pdf_loader(self, filepath, *args, **kwargs):
        return UnstructuredPDFLoader(filepath)
    

# if __name__ == "__main__":
#     loader = DocumentLoader()
#     text_loader_obj = loader.text_loader(filepath="")
#     text_documents = text_loader_obj.load()
#     print(text_documents)