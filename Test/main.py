'''O firma e organizata in departamente, fiecare departament avand angajati din 3 categorii: Manager,Programator si Tester.
Firma si departamentul au ca si atribut nume, iar angajatii au nume, salar.
Construiti structura necesara pentru a putea adauga la o firma departamente, subdepartamente, etc... si angajati.
Realizati o operatie de calculare a salariului platit pentru fiecare categorie de angajati, precum si totalul tuturor angajatilor'''
from Firma import Firma
from Departament import Departament
from Manager import Manager
from Programator import Programator
from Tester import Tester
from VisitorSalar import VisitorSalar


def main():
    a=Firma('Nokia')
    d=Departament('5G')

    d.add(Manager('Ionescu',10000))
    d.add(Programator('Popescu',15000))
    d.add(Programator('Popa',45000))
    d.add(Tester('Adam',20000))

    a.add(d)
    calculSalar=VisitorSalar()
    a.accept(calculSalar)
    calculSalar.print()


if __name__=='__main__':
    main()