from Element import Element
from Visitee import Visitee

class Departament(Element,Visitee):
    def __init__(self,nume):
        self.__nume=nume
        self.__elemente:list[Element]=[]

    def add(self,element):
        self.__elemente.append(element)

    def get(self):
        return self.__elemente

    def accept(self, visitor):
        visitor.visitDepartament(self)
