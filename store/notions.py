import json as j


class Notion:
    def __init__(self, _sum, _data, _method):
        self._sum = _sum
        self._data = _data
        self._method = _method

    def __str__(self):
        return f"_sum: {self._sum} | _data: {self._data} | _method: {self._method}"

    def json(self, dumped=True):
        return j.dumps(self.__dict__) if dumped else self.__dict__


class Enrollment(Notion):
    def __init__(self, _sum, _data, _method):
        super().__init__(_sum, _data, _method)
        self.type = Enrollment


class Withdrawal(Notion):
    def __init__(self, _sum, _data, _method):
        super().__init__(_sum, _data, _method)
        self.type = Withdrawal
