# person-extractor
Work in Progress: Identify People's Names in Text

# usage
You initialize a PersonExtractor with a path to a CSV of names with each column a language.
You can create a csv through [Wikinames](https://github.com/mak4lab/wikinames).

```python
from person_extractor import PersonExtractor

text = "John Doe and Jane Doe live in Springfield"

extractor = PersonExtractor(data="names.csv")

people = extractor.extract(text)
```

extract returns a list of objects:
```python
[
    { "text": "John Doe", "start": 0, "end": 7 },
    { "text": "Jane Doe", "start": 13, "end": 20 }
]
```

# test
To test the package run:
```
python -m unittest person_extractor.test
```

# contact
Post an issue at https://github.com/Mak4Lab/person-extractor/issues or email the package authors at daniel@mak4lab.com and victoria@mak4lab.com 
