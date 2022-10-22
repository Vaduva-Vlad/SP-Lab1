from Book import Book
from Author import Author
from Section import Section
from Paragraph import Paragraph
from Image import Image


def main():
    noapteBuna = Book('Noapte buna, copii!')
    rpGheo = Author("Radu Pavel Gheo")
    noapteBuna.addAuthor(rpGheo)

    cap1 = Section("Capitolul 1")
    cap11 = Section("Capitolul 1.1")
    cap111 = Section("Capitolul 1.1.1")
    cap1111 = Section("Capitolul 1.1.1.1")
    noapteBuna.addContent(Paragraph("Multumesc celor care..."))
    noapteBuna.addContent(cap1)
    cap1.add(Paragraph("Moto capitol"))
    cap1.add(cap11)
    cap11.add(Paragraph("Text from subchapter 1.1"))
    cap11.add(cap111)
    cap111.add(Paragraph("Text from subchapter 1.1.1"))
    cap111.add(cap1111)
    cap1111.add(Image("Image subchapter 1.1.1.1"))

    noapteBuna.print()


if __name__ == '__main__':
    main()
