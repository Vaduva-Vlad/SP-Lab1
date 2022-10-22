from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def get(self):
        pass
