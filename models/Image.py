from models.Element import Element
from models.Picture import Picture
from models.Visitee import Visitee
from io import BytesIO
from services.ImageLoaderFactory import ImageLoaderFactory
import time


class Image(Element, Picture,Visitee):
    def __init__(self, url, dim):
        self.__url = url
        self.__dim = dim
        self.__content = None
        self.__uses: ImageLoaderFactory
        try:
            time.sleep(5)
        except Exception as e:
            print(e)

    def url(self):
        return self.__url

    def dim(self):
        return self.__dim()

    def content(self):
        return self.__content

    def add(self, content):
        self.__content = content

    def remove(self, content=None):
        self.__content = None

    def get(self, content=None):
        return self.__content

    def print(self):
        print(f"Image with url: {self.__url}")

    def accept(self,visitor):
        visitor.visitImage(self)