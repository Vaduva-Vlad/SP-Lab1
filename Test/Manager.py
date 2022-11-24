from Element import Element
from Visitee import Visitee

class Manager(Element,Visitee):
    def __init__(self,nume,salar):
        self.__nume=nume
        self.__salar=salar

    def get(self):
        return self.__salar

    def accept(self, visitor):
        visitor.visitManager(self)