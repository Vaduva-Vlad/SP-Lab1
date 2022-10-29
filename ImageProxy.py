from Element import Element
from Image import Image

class ImageProxy(Element):
    def __init__(self,url,dim):
        self.url=url
        self.dim=dim
        self.realImage=None

    def loadImage(self):
        if self.realImage is None:
            self.realImage=Image(self.url)
        return self.realImage
