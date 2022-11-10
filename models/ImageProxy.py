from Element import Element
from Image import Image
from Picture import Picture


class ImageProxy(Element, Picture):
    def __init__(self, url):
        self.__url = url
        self.__dim=''
        self.__realImage = None

    def loadImage(self):
        if self.__realImage is None:
            self.__realImage = Image(self.__url,self.__dim)
        return self.__realImage

    def url(self):
        return self.__url

    def dim(self):
        return self.__dim()

    def content(self):
        return self.__realImage

    def add(self, content):
        self.__url = content

    def remove(self, content=None):
        self.__url = None
        self.__dim = None
        self.__realImage = None

    def get(self, content=None):
        return self.__realImage

    def print(self):
        self.loadImage()
        self.__realImage.print()