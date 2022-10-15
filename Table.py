from Element import Element
class Table(Element):
    def __init__(self, title):
        self.__title: str = title

    def print(self):
        print(f"Table with title: {self.__title}")
