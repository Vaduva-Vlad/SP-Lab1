from models.Element import Element
from models.Visitee import Visitee
import copy

class Section(Element,Visitee):
    def __init__(self, title: str):
        self._title: str = title
        self._children: list[Element] = []

    def add(self,content):
        new_content=copy.deepcopy(content)
        self._children.append(new_content)
        return new_content

    def remove(self,idx):
        self._children.pop(idx)

    def get(self,idx):
        return self._children[idx]

    def print(self):
        print(self._title)
        for child in self._children:
            child.print()

    def accept(self,visitor):
        visitor.visitSection(self)