import json

class complexEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.toJSON()
                
