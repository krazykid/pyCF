from CFObject import CFObject

class resourceType(CFObject):
    def __init__(self):
        pass

    def toJSON(self):
        return self.__dict__
