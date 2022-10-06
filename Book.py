class Book:
    def __init__(self,title):
        self.title=title
        self.paragraphs=[]
        self.images=[]
        self.tables=[]
        self.contents=''

    def createNewParagraph(self,paragraph):
        self.paragraphs.append(paragraph)
        self.contents+=paragraph+'\n'

    def createNewImage(self,image):
        self.images.append(image)
        self.contents+=image+'\n'

    def createNewTable(self,table):
        self.tables.append(table)
        self.contents+=table+'\n'

    def printBook(self):
        print(self.contents)