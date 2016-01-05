from resourceProperty import resourceProperty

class portRangeProperty(resourceProperty):

    def __init__(self, fromPort, toPort):
        self.fromPort = fromPort
        self.toPort = toPort

    def toJSON(self):
        retDict = {}
        retDict["From"] = self.fromPort
        retDict["To"] = self.toPort
        return retDict
    

