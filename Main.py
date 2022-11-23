from models.ImageProxy import ImageProxy
from models.Section import Section
from models.Paragraph import Paragraph
from models.Image import Image
from models.Table import Table
from models.RenderContentVisitor import RenderContentVisitor

from services.AlignLeft import AlignLeft
from services.AlignRight import AlignRight
from services.AlignCenter import AlignCenter


def main():
    cap1 = Section("Capitolul 1")
    p1 = Paragraph("Paragraph 1")
    cap1.add(p1)
    p2 = Paragraph("Paragraph 2")
    cap1.add(p2)
    p3 = Paragraph("Paragraph 3")
    cap1.add(p3)
    p4 = Paragraph("Paragraph 4")
    cap1.add(p4)

    cap1.add(ImageProxy("ImageOne"))
    cap1.add(Image("ImageTwo",0))
    cap1.add(Paragraph("Some text"))
    cap1.add(Table("Table 1"))

    stats=RenderContentVisitor()
    cap1.accept(stats)
    stats.printStats()


if __name__ == '__main__':
    main()
