from Visitor import Visitor


class VisitorSalar(Visitor):
    def __init__(self):
        self.__salariuTotal: int = 0
        self.__salariuProgramator: int = 0
        self.__salariuManager: int = 0
        self.__salariuTester: int = 0

    def visitFirma(self,firma):
        for dep in firma.get():
            dep.accept(self)

    def visitDepartament(self,departament):
        for el in departament.get():
            el.accept(self)

    def visitProgramator(self, programator):
        salar = programator.get()
        self.__salariuProgramator += salar
        self.__salariuTotal += salar

    def visitManager(self, manager):
        salar = manager.get()
        self.__salariuManager += salar
        self.__salariuTotal += salar

    def visitTester(self, tester):
        salar = tester.get()
        self.__salariuTester += salar
        self.__salariuTotal += salar

    def print(self):
        print(f"Salariu total: {self.__salariuTotal}")
        print(f"Salariu total Manager: {self.__salariuManager}")
        print(f"Salariu total Programator {self.__salariuProgramator}")
        print(f"Salariu total Tester: {self.__salariuTester}")
