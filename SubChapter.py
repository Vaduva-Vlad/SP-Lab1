from Paragraph import Paragraph
from Image import Image
from Table import Table
from Element import Element


class SubChapter:
    def __init__(self, name):
        self.__name: str = name
        self.__elements: list[Element] = []
        """self.__paragraphs: list[Paragraph] = []
        self.__images: list[Image] = []
        self.__tables: list[Table] = []"""

    def createNewParagraph(self, text):
        paragraph = Paragraph(text)
        self.__elements.append(paragraph)
        return len(self.__elements) - 1

    def createNewImage(self, imageName):
        image = Image(imageName)
        self.__elements.append(image)
        return len(self.__elements) - 1

    def createNewTable(self, title):
        table = Table(title)
        self.__elements.append(table)
        return len(self.__elements) - 1

    def print(self):
        print(f"""Subchapter: {self.__name}""")
        for element in self.__elements:
            element.print()