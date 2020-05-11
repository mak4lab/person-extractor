# person-extractor
Work in Progress: Identify People's Names in Text

# usage
You initialize a PersonExtractor with a path to a CSV of names with each column a language.
You can create a csv through [Wikinames](https://github.com/mak4lab/wikinames).

```python
from person_extractor import PersonExtractor

text = "Але дістатися на роботу працівникам цих бізнесів, якщо у них немає власного автомобіля або грошей на таксі чи корпоративну розвозку, стане справжньою проблемою, прогнозує політолог Микола Давидюк."

extractor = PersonExtractor(data="names.csv")

people = extractor.extract(text)
```

extract returns a list of objects:
```python
    [
        {
            'start': 336,
            'end': 343,
            'text': 'Давидюк',
            'spellings': {
                'en': 'Davidyuk',
                'uk': 'Давидюк'
            }
        }
    ]
```

# test
To test the package run:
```
python -m unittest person_extractor.test
```

# contact
Post an issue at https://github.com/Mak4Lab/person-extractor/issues or email the package authors at daniel@mak4lab.com and victoria@mak4lab.com 
