from Element import Element


class Section:
    def __init__(self, title: str):
        self.__title: str = title
        self.__children: list[Element] = []

    def add(self,content):
        self.__children.append(content)

    def print(self):
        print(self.__title)
        for child in self.__children:
            child.print()