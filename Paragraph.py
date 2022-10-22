from Element import Element
class Paragraph(Element):
    def __init__(self,text):
        self.__text: str=text

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass

    def print(self):
        print(f"Paragraph: {self.__text}")
