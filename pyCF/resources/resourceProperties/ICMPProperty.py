from resourceProperty import resourceProperty

class ICMPProperty(resourceProperty):

    def __init__(self, ICMPCode, ICMPType):
        self.ICMPCode = ICMPCode
        self.ICMPType = ICMPType

    def toJSON(self):
        retDict = {}
        retDict["Code"] = self.ICMPCode
        retDict["Type"] = self.ICMPType
        return retDict
    

