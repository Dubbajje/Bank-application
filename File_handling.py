import os
import json

class File:

    @staticmethod
    def write_to_file(dict):
        File.create_file()
        json_string = json.dumps(dict)
        file = open("mappmapp/database.json", "w")
        file.write(json_string)
        file.close()

    @staticmethod
    def create_file():
        if not os.path.exists("mappmapp"):
            os.mkdir("mappmapp")



