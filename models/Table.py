from models.Element import Element
from models.Visitee import Visitee


class Table(Element, Visitee):
    def __init__(self, title):
        self.__title: str = title
        self.rows = []

    def add(self, row):
        self.rows.append(row)

    def remove(self, rowIdx):
        self.rows.pop(rowIdx)

    def get(self, rowIdx):
        return self.rows[rowIdx]

    def print(self):
        print(f"Table with title: {self.__title}")

    def accept(self, visitor):
        visitor.visitTable(self)
