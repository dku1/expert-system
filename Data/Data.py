import json


class Data:
    def __init__(self, path):
        self.path = path
        self.data = self.load()

    def load(self):
        try:
            with open(self.path, encoding='utf-8') as json_file:
                return json.load(json_file)
        except ImportError:
            raise ImportError.path

    def save(self, obj):
        try:
            with open(self.path, 'w', encoding='utf-8') as json_file:
                json.dump(obj, json_file, indent=2, ensure_ascii=False)
        except ImportError:
            raise ImportError.path

    def get(self):
        return self.data
