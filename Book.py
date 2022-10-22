from Author import Author
from Element import Element


class Book:
    def __init__(self, title):
        self.__title: str = title
        self.__authors: list[Author] = []
        self.__elements: list[Element] = []

    def addAuthor(self, author: Author):
        self.__authors.append(author)

    def addContent(self, content):
        self.__elements.append(content)

    def print(self):
        print(f"Book: {self.__title}\n")
        print("Authors:")
        for author in self.__authors:
            author.print()
        print("")

        for element in self.__elements:
            element.print()
