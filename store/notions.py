import json as j
from datetime import datetime
from typing import Any


class Notion:
    str_datetime_sample = "%Y.%m.%d-%H:%M:%S"

    def __init__(self, id, _datetime, _sum, _method):
        self.id = id
        self._datetime = _datetime
        self._sum = _sum
        self._method = _method

    def __str__(self):
        return f"_sum: {self._sum} | id: {self.id} | _method: {self._method} | _datetime: {self._datetime}"

    def __eq__(self, other):
        data1 = self.json(dumped=False)
        data2 = other.json(dumped=False)
        data1.pop("_id")
        data2.pop("_id")
        return data1 == data2

    def json(self, dumped=True):
        data = self.__dict__.copy()
        data["_datetime"] = data["_datetime"].strftime(self.str_datetime_sample)
        return j.dumps(data) if dumped else data

    @classmethod
    def from_dict(cls, data_dict):
        data_dict["_datetime"] = datetime.strptime(data_dict["_datetime"], cls.str_datetime_sample)
        return cls(**data_dict)

    def update(self, data: dict[str, Any]) -> None:
        self.__init__(**data)

