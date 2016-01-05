class invalidNetworkACLEntryError(Exception):
    """invalidNetworkACLEntryError is thrown when networkACLEntry is improperly instantiated"""

    def __init__(self, CFName, msg):
        self.CFName = CFName
        self.msg = msg

    def __str__(self):
        return self.CFName + ": " + self.msg
                                        
