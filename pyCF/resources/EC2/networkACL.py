from resourceType import resourceType

class networkACL(resourceType):
    def __init__(self, CFName, VPCID, tagDict={}):
        self.CFName = CFName
        self.CFType = "AWS::EC2::NetworkAcl"
        self.VPCID = VPCID
        self.tagDict = tagDict

    def toJSON(self):
        retDict = {}
        retDict[self.CFName] = {}
        retDict[self.CFName]["Type"] = self.CFType
        retDict[self.CFName]["Properties"] = {}
        retDict[self.CFName]["Properties"]["VpcId"] = self.VPCID
        retDict[self.CFName]["Properties"]["Tags"] = []
        for key, value in self.tagDict.iteritems():
            newPair = {}
            newPair["Key"] = key
            newPair["Value"] = value
            retDict[self.CFName]["Properties"]["Tags"].append(newPair)

        return retDict
