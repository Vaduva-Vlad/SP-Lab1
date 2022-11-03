from Book import Book
from Section import Section
from ImageProxy import ImageProxy
import time
from Paragraph import Paragraph
from AlignLeft import AlignLeft
from AlignRight import AlignRight
from AlignCenter import AlignCenter


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

    print("Printing without alignment\n")
    cap1.print()

    cap1.get(0).setAlignStrategy(AlignCenter())
    cap1.get(1).setAlignStrategy(AlignRight())
    cap1.get(3).setAlignStrategy(AlignLeft())

    print("Printing with alignment\n")

    cap1.print()


if __name__ == '__main__':
    main()
