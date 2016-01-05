from resourceType import resourceType
from networkACL import networkACL
from resourceErrors import invalidNetworkACLEntryError

class networkACLEntry(resourceType):
    """http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-network-acl-entry.html"""

    def __init__(self, CFName, networkACL, CIDRBlock, protocol, egress, ruleAction, ruleNumber, ICMP=None, portRange=None):
        self.CFName = CFName
        self.CFType = "AWS::EC2::NetworkAclEntry"
        self.networkACL = networkACL
        self.CIDRBlock = CIDRBlock
        self.protocol = protocol
        self.egress = egress
        self.ruleAction = ruleAction
        self.ruleNumber = ruleNumber
        self.ICMP = ICMP
        self.portRange = portRange

        if (self.protocol == 1) and (ICMP == None):
            raise invalidNetworkACLEntryError(self.CFName, "ICMP protocol specified, but no code/type specified")

        if (self.protocol == 6) and (portRange == None):
            raise invalidNetworkACLEntryError(self.CFName, "TCP protocol specified, but no port range specified")

        if (self.protocol == 17) and (ICMP == None):
            raise invalidNetworkACLEntryError(self.CFName, "UDP protocol specified, but no port range specified")

    def toJSON(self):
        retDict = {}
        retDict[self.CFName] = {}
        retDict[self.CFName]["Type"] = self.CFType
        retDict[self.CFName]["Properties"] = {}
        if isinstance(self.networkACL, networkACL):
            retDict[self.CFName]["NetworkAclId"] = self.networkACL.toRef()
        elif isinstance(self.networkACL, String):
            # TODO: Your mind wandered somewhere else...
            pass
        retDict[self.CFName]["Properties"]["CidrBlock"] = self.CIDRBlock
        retDict[self.CFName]["Properties"]["Protocol"] = self.protocol
        retDict[self.CFName]["Properties"]["Egress"] = self.egress
        retDict[self.CFName]["Properties"]["RuleAction"] = self.ruleAction
        retDict[self.CFName]["Properties"]["RuleNumber"] = self.ruleNumber
        if self.ICMP != None:
            retDict[self.CFName]["Properties"]["Icmp"] = self.ICMP
        if self.portRange != None:
            retDict[self.CFName]["Properties"]["PortRange"] = self.portRange

        return retDict
