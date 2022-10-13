from SubChapter import SubChapter


class Chapter:
    def __init__(self, name):
        self.__name:str = name
        self.__subchapters: list[SubChapter] = []

    def createSubChapter(self, name):
        subchapter = SubChapter(name)
        self.__subchapters.append(subchapter)
        return len(self.__subchapters)-1

    def getSubChapter(self,idx):
        return self.__subchapters[idx]

    def printChapter(self):
        print(self.__name)
