from abc import ABC, abstractmethod

#interfata
class Element(ABC):
    @abstractmethod
    def get(self):
        pass