from os.path import dirname, realpath

directory_of_this_file = dirname(realpath(__file__))

class PersonExtractor:

    def __init__(self, languages):
        self.names = set()

    def extract_people(self):
        return [
            {
                "start": 0,
                "end": 7,
                "text": "John Doe"
            }
        ]
