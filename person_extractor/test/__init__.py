from os.path import dirname, join, realpath
from unittest import TestCase

from person_extractor import PersonExtractor

directory_of_this_file = dirname(realpath(__file__))
test_data_dir = join(directory_of_this_file, 'data')

class ExtractionMethods(TestCase):
    def test_extraction(self):
        test_file_path = join(test_data_dir, 'en-uk_names.csv')

        extractor = PersonExtractor(data=test_file_path)
        text = """
        Прем'єр-міністр Денис Шмигаль заявив, що метро не запрацює щонайменше до 22 травня. Але, цілком можливо, що і це не кінцева дата.

        Але дістатися на роботу працівникам цих бізнесів, якщо у них немає власного автомобіля або грошей на таксі чи корпоративну розвозку, стане справжньою проблемою, прогнозує політолог Микола Давидюк.

        Гліб Вишлінський, виконавчий директор Центру економічної стратегії, називає це "карантином для бідних".
        """
        people = extractor.extract_people(text)
        print("people:", people)
        self.assertGreaterEqual(len(people), 1)
        person = next(p for p in people if p['text'] == 'Давидюк')
        self.assertEqual(person['spellings']['en'], 'Davidyuk')
