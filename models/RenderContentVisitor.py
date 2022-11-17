from services.Visitor import Visitor

class RenderContentVisitor(Visitor):
    def __init__(self):
        self.visitedParagraphs=0
        self.visitedImages=0
        self.visitedTables=0

    def visitBook(self, book):
        pass

    def visitSection(self, section):
        pass

    def visitTableOfContents(self, tableofcontents):
        pass

    def visitParagraph(self, paragraph):
        self.visitedParagraphs+=1

    def visitImage(self, image):
        self.visitedImages+=1

    def visitTable(self, table):
        self.visitedTables+=1