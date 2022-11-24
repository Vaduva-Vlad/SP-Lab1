from Element import Element
from Visitee import Visitee

class Firma(Element,Visitee):
    def __init__(self,nume):
        self.__nume=nume
        self.__elemente:list[Element]=[]

    def add(self,departament):
        self.__elemente.append(departament)

    def get(self):
        return self.__elemente

    def accept(self, visitor):
        visitor.visitFirma(self)