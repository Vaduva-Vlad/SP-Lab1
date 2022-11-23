from services.AlignStrategy import AlignStrategy

class AlignCenter(AlignStrategy):
    def render(self,paragraph):
        return '####'+paragraph+'####'