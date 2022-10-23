from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def add(self,content):
        pass

    @abstractmethod
    def remove(self,content):
        pass

    @abstractmethod
    def get(self,content):
        pass
