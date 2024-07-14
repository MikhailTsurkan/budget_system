import json as j
from datetime import datetime
from store.mixins import DateTimeIdInit


class Notion(DateTimeIdInit):
    id_field_name = "time"
    id_field_name_callable = True

    def __init__(self, _datetime, _sum=None, _method=None):
        super().__init__(_datetime)
        self._sum = _sum
        self._method = _method

    def __str__(self):
        return f"_sum: {self._sum} | id: {self.id} | _method: {self._method}"

    def json(self, dumped=True):
        return j.dumps(self.__dict__) if dumped else self.__dict__


class Enrollment(Notion):
    def __init__(self, _sum, _data, _method):
        super().__init__(_sum, _data, _method)
        self.type = "enrollment"


class Withdrawal(Notion):
    def __init__(self, _sum, _data, _method):
        super().__init__(_sum, _data, _method)
        self.type = "withdrawal"
