import json


class DataBase(object):
    # Inits the database with a provided json
    def __init__(self, file):
        self.file = file
        with open(file, 'r+') as json_file:
            self.data = json.load(json_file)

    # Returns a name, a picture and a price for the
    # provided codes (or None if not found)
    def fetch(self, code):
        if code in self.data.keys():
            return self.data[code]
        return ["", "", ""]
