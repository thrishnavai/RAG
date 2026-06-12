from abc import ABC, abstractmethod
from typing import Optional, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter,CharacterTextSplitter,TextSplitter, MarkdownTextSplitter
from langchain_text_splitters.python import PythonCodeTextSplitter
from langchain_text_splitters.nltk import NLTKTextSplitter

class Splitter(ABC):
    def __init__(self):
        pass

    @abstractmethod    
    def recursive_character_text_splitter(self, chunksize, chunkoverlap, *args, **kwargs):
        pass
    
    @abstractmethod    
    def character_text_splitter(self, separator, chunksize, chunkoverlap, *args, **kwargs):
        pass

    @abstractmethod    
    def text_splitter(self, separator, chunksize, chunkoverlap, *args, **kwargs):
        pass

    @abstractmethod    
    def markdown_text_splitter(self, chunksize, chunkoverlap, *args, **kwargs):
        pass

    @abstractmethod    
    def python_code_text_splitter(self, chunksize, chunkoverlap, *args, **kwargs):
        pass

    @abstractmethod    
    def nltk_text_splitter(self, chunksize, chunkoverlap, *args, **kwargs):
        pass

class TextSplitter(Splitter):
    
    def __init__(self):
        super().__init__()
        pass
    
    def recursive_character_text_splitter(self, chunksize, chunkoverlap, *args, **kwargs):
        return RecursiveCharacterTextSplitter(chunksize, chunkoverlap)
    
    def character_text_splitter(self, separator, chunksize, chunkoverlap, *args, **kwargs):
        return CharacterTextSplitter(separator, chunksize, chunkoverlap)
    
    def text_splitter(self, separator, chunksize, chunkoverlap, *args, **kwargs):
        return TextSplitter(separator, chunksize, chunkoverlap)
    
    def markdown_text_splitter(self, separator, chunksize, chunkoverlap, *args, **kwargs):
        return MarkdownTextSplitter(separator, chunksize, chunkoverlap)
    
    def python_code_text_splitter(self, chunksize, chunkoverlap, *args, **kwargs):
        return PythonCodeTextSplitter(chunksize, chunkoverlap, *args, **kwargs)
    
    def nltk_text_splitter(self, chunksize, chunkoverlap, *args, **kwargs):
        return NLTKTextSplitter(chunksize, chunkoverlap, *args, **kwargs)

# if __name__ == "__main__":
#     splitter = TextSplitter()
#     text_splitter_obj = splitter.recursive_character_text_splitter(chunksize, chunkoverlap)
#     text_split_data = text_splitter_obj.load()
#     print(text_documents)