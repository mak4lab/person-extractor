from csv import DictReader
from os.path import dirname, realpath
from re import search

directory_of_this_file = dirname(realpath(__file__))

class PersonExtractor:

    def __init__(self, data):
        self.names = set()
        with open(data) as f:
            for line in DictReader(f):
                for language, name in line.items():
                    if name:
                        self.names.add(name)

    def extract_people(self, text):
        results = []
        for name in self.names:
            if name in text:
                match = search(name, text)
                results.append({ "start": match.start(), "end": match.end(), "text": name })
        return results


