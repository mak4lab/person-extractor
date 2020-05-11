from csv import DictReader
from os.path import dirname, realpath
from re import finditer

directory_of_this_file = dirname(realpath(__file__))

class PersonExtractor:

    def __init__(self, data):
        self.names = []
        with open(data) as f:
            for line in DictReader(f):
                name = {}
                for language, name_in_language in line.items():
                    if name_in_language:
                        name[language] = name_in_language
                self.names.append(name)

    def extract_people(self, text):
        results = []
        for name in self.names:
            for spelling in name.values():
                if spelling in text:
                    for match in finditer(spelling, text):
                        results.append({
                            "start": match.start(),
                            "end": match.end(),
                            "text": spelling,
                            "spellings": name
                        })
        return results


