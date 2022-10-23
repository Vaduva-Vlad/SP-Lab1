from Element import Element
from io import BytesIO


class Image(Element):
    def __init__(self, imageName):
        self.__imageName: str = imageName
        self.__bytes=None

    def add(self,content):
        self.__bytes=content

    def remove(self,content=None):
        self.__bytes=None

    def get(self,content=None):
        return self.__bytes

    def print(self):
        print(f"Image with name: {self.__imageName}")
