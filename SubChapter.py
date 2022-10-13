from Paragraph import Paragraph
from Image import Image
from Table import Table


class SubChapter:
    def __init__(self, name):
        self.__name: str = name
        self.__paragraphs: list[Paragraph] = []
        self.__images: list[Image] = []
        self.__tables: list[Table] = []

    def createNewParagraph(self, text):
        paragraph = Paragraph(text)
        self.__paragraphs.append(paragraph)
        return len(self.__paragraphs) - 1

    def createNewImage(self, imageName):
        image = Image(imageName)
        self.__images.append(image)
        return len(self.__images) - 1

    def createNewTable(self, title):
        table = Table(title)
        self.__tables.append(table)
        return len(self.__tables) - 1

    def printSubChapter(self):
        print(f"""Subchapter: {self.__name}""")
