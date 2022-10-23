from Element import Element


class Paragraph(Element):
    def __init__(self, text):
        self.__text: str = text

    def add(self, text):
        self.__text += text

    def remove(self, bounds):
        start = bounds[0]
        end = bounds[1]
        self.__text = self.__text[:start] + self.__text[end:]

    def get(self, idx):
        return self.__text[idx:]

    def print(self):
        print(f"Paragraph: {self.__text}")
