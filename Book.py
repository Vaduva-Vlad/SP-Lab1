from Author import Author
from Chapter import Chapter


class Book:
    def __init__(self, title):
        self.__title: str = title
        self.__author: Author
        self.__chapters: list[Chapter] = []

    def addAuthor(self, author: Author):
        self.__author = author

    def createChapter(self, name):
        chapter = Chapter(name)
        self.__chapters.append(chapter)
        return len(self.__chapters) - 1

    def getChapter(self, idx):
        return self.__chapters[idx]
