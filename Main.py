from Book import Book
from Author import Author
from Section import Section
from Paragraph import Paragraph
from Image import Image
import time


def main():
    t=time.time()
    startTime=int(t*1000)
    img1=Image('Pamela Anderson')
    img2=Image('Kim Kardashian')
    img3=Image('Kirby Griffin')
    playboys1=Section('Front Cover')
    playboys1.add(img1)
    playboys2=Section('Summer Girls')
    playboys2.add(img2)
    playboys2.add(img3)

    playboy=Book('Playboy')
    playboy.addContent(playboys1)
    playboy.addContent(playboys2)

    endTime=int(time.time()*1000)
    print(f'Creation of the content book: {endTime-startTime} milliseconds')

    startTime=int(time.time()*1000)
    playboys1.print()
    endTime=int(time.time()*1000)
    print(f'Printing of the section 1 took: {endTime-startTime} milliseconds')

    startTime=int(time.time()*1000)
    print(f'Printing again the section 1 took {endTime-startTime} milliseconds')

if __name__ == '__main__':
    main()
