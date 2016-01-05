import json
from resources.resourceType import resourceType
from pyCFErrors import InvalidResourceObjectError

class pyCF:
    AWSTemplateFormatVersion = ""
    description = ""
    metadata = {}
    parameters = {}
    mappings = {}
    resources = {}
    outputs = {}

    def __init__(self, description="", AWSTemplateFormatVersion = "2010-09-09"):
        self.description = description
        self.AWSTemplateFormatVersion = AWSTemplateFormatVersion

    def add_resource(self, resource):
        if not isinstance(resource, resourceType):
            raise InvalidResourceObjectError(resource, "Not a resourceType object")
        if resource.name in self.resources:
            raise InvalidResourceObjectError(resource, "Object already exists in Resources dictionary")
        self.resources[resource.name] = resource


    def toJSON(self):
        retDict = {}
        retDict['AWSTemplateFormatVersion'] = self.AWSTemplateFormatVersion
        retDict['Description'] = self.description
        retDict['Metadata'] = self.metadata
        retDict['Parameters'] = self.parameters
        retDict['Mappings'] = self.mappings
        retDict['Resources'] = self.resources
        retDict['Outputs'] = self.outputs
        return retDict
    
    
    
