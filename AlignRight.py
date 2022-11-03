from AlignStrategy import AlignStrategy

class AlignRight(AlignStrategy):
    def render(self,paragraph):
        return '######' + paragraph