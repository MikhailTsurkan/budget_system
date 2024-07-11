import json as j
from datetime import datetime


class Notion:
    def __init__(self, _sum, _data, _method):
        self._sum = _sum
        self.id = datetime.now().time()
        self._method = _method

    def __str__(self):
        return f"_sum: {self._sum} | id: {self.id} | _method: {self._method}"

    def json(self, dumped=True):
        return j.dumps(self.__dict__) if dumped else self.__dict__
