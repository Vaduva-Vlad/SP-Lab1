from Element import Element
class Image(Element):
    def __init__(self, imageName):
        self.imageName: str = imageName

    def print(self):
        print(f"Image with name: {self.imageName}")