from abc import ABC, abstractmethod


# interfata
class Visitee(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass
