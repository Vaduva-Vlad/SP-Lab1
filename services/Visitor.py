from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visitBook(self,book):
        pass

    @abstractmethod
    def visitSection(self,section):
        pass

    @abstractmethod
    def visitTableOfContents(self,tableofcontents):
        pass

    @abstractmethod
    def visitParagraph(self,paragraph):
        pass

    @abstractmethod
    def visitImage(self,image):
        pass

    @abstractmethod
    def visitTable(self,table):
        pass