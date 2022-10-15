from Element import Element
class Paragraph(Element):
    def __init__(self,text):
        self.__text: str=text

    def print(self):
        print(f"Paragraph: {self.__text}")
