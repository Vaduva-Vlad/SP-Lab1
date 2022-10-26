from Author import Author
from Element import Element
from Section import Section
import copy


class Book(Section):
    def __init__(self, title):
        super().__init__(title)
        self.__authors: list[Author] = []

    def addAuthor(self, author: Author):
        self.__authors.append(author)

    def addContent(self, content):
        new_content = copy.deepcopy(content)
        self._children.append(new_content)
        return new_content

    def print(self):
        print(f"Book: {self._title}\n")
        print("Authors:")
        for author in self.__authors:
            author.print()
        print("")

        for element in self._children:
            element.print()
