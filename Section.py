from Element import Element


class Section(Element):
    def __init__(self, title: str):
        self.__title: str = title
        self.__children: list[Element] = []

    def add(self,content):
        self.__children.append(content)

    def remove(self,idx):
        self.__children.pop(idx)

    def get(self,idx):
        return self.__children[idx]

    def print(self):
        print(self.__title)
        for child in self.__children:
            child.print()