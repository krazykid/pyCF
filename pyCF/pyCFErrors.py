class InvalidResourceObjectError(Exception):
    """InvalidResourceObjectError is thrown when trying to add a non-resource object to the Resources dictionary of pyCF"""

    def __init__(self, obj, msg):
        self.obj = obj
        self.msg = msg


    def __str__(self):
        return "Invalid object (" + self.obj + "): " + self.msg
    
                                            
    
