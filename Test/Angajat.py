from abc import ABC, abstractmethod

#interfata
class Angajat(ABC):
    def __init__(self,nume,salar):
        self.__nume:int=nume
        self.__salar:int=salar

    @abstractmethod
    def getSalariu(self):
        pass
