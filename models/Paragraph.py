from Element import Element


class Paragraph(Element):
    def __init__(self, text):
        self.__text: str = text
        self.textAlignment=None

    def add(self, text):
        self.__text += text

    def remove(self, bounds):
        start = bounds[0]
        end = bounds[1]
        self.__text = self.__text[:start] + self.__text[end:]

    def get(self, idx):
        return self.__text[idx:]

    def setAlignStrategy(self,strategy):
        self.textAlignment=strategy

    def print(self):
        if self.textAlignment is not None:
            print(f"Paragraph: {self.textAlignment.render(self.__text)}")
        else:
            print(self.__text)

    def accept(self,visitor):
        visitor.visitParagraph(self)