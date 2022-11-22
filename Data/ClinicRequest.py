import urllib.parse
import json
from urllib.request import urlopen
from urllib.error import HTTPError


class ClinicRequest:
    def __init__(self):
        self.base_url = 'https://search-maps.yandex.ru/v1/?'
        self.type = 'biz'
        self.lang = 'ru_RU'
        self.results = '1'
        self.api_key = 'cc058527-7447-43cf-8e36-1ce6e40bddee'

    def get(self, city, outside):
        clinicData = self.search(city, outside)
        return json.load(clinicData)['features'][0]['properties']['CompanyMetaData']

    def search(self, city, outside):
        try:
            text = f'Диагностический центр, {city}, {outside}'

            params = urllib.parse.urlencode(
                {'text': text, 'type': self.type, 'lang': self.lang, 'results': self.results, 'apikey': self.api_key})

            url = self.base_url + params
            response = urllib.request.urlopen(url)

            return response
        except HTTPError:
            raise HTTPError
