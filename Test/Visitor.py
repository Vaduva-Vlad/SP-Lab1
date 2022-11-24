from abc import ABC, abstractmethod


# interfata
class Visitor(ABC):
    @abstractmethod
    def visitProgramator(self, programator):
        pass

    @abstractmethod
    def visitManager(self, manager):
        pass

    @abstractmethod
    def visitTester(self, tester):
        pass

    @abstractmethod
    def visitFirma(self, tester):
        pass

    @abstractmethod
    def visitDepartament(self, tester):
        pass