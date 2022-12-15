class DocumentManager:

    __create_key = object()
    __instance=None

    @classmethod
    def getInstance(self,cls, value):
        if self.__instance is None:
            inst=DocumentManager(cls.__create_key, value)
            self.__instance=inst
            return inst


    def __init__(self, create_key, book):
        if create_key!=DocumentManager.__create_key:
            print("Constructor must be called using getInstance() method")
            return
        self.book=book