from Element import Element


class Image(Element):
    def __init__(self, imageName):
        self.imageName: str = imageName

    def add(self):
        pass

    def remove(self):
        pass

    def get(self):
        pass

    def print(self):
        print(f"Image with name: {self.imageName}")
