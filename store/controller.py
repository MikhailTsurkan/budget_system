import os
import json as j
from datetime import datetime
from typing import Any

from store.notions import Notion


class GetException(Exception):
    pass


class ManyReturnException(GetException):
    pass


class DoesNotExist(GetException):
    pass


class Manager:
    _class = Notion
    current_id = 1

    def __init__(self, data):
        self.data = data

    def create(self, _sum, _method):
        now = datetime.now()

        _id = self.current_id

        obj = self._class(_id, now, _sum, _method)
        self.data.append(obj)
        self.current_id += 1
        return obj

    def get(self,many=True, **kwargs):
        data = self.data.copy
        for k, v in kwargs.items():
            for i in data:
                if getattr(i, k) != v:
                    data.remove(i)
        if many:
            return data
        if len(data) > 1:
            raise ManyReturnException
        elif len(data) < 1:
            raise DoesNotExist

        return data.pop()

    def update(self,notion, data: dict[str, Any]) -> None:
        notion.update(data)

    def delete(self, notion):
        self.data.remove(notion)

    def get_metadata(self):
        return {
            "current_id": self.current_id
        }

    def set_metadata(self, data_dict):
        for k, v in data_dict.items():
            setattr(self, k, v)


class Controller:
    def __init__(self, notions):
        self.notions = notions
        self.manager = Manager(self.notions)

    def json(self, dumped=True):
        to_save = []

        for notion in self.notions:
            to_save.append(notion.json(dumped=False))

        data_to_save = {
            "metadata": self.manager.get_metadata(),
            "notions": to_save
        }

        return j.dumps(data_to_save, indent=2) if dumped else data_to_save

    def create_file(self, dirname):
        path = os.path.join(dirname, "data.json")
        with open(path, "w") as f:
            f.write(self.json())

    @classmethod
    def from_dict(cls, data_dict):
        notions = [Notion.from_dict(notion_dict) for notion_dict in data_dict["notions"]]
        contr = cls(notions)
        contr.manager.set_metadata(data_dict["metadata"])
        return contr

    @classmethod
    def from_file(cls, path):
        with open(path, "r") as f:
            string = f.read()
        if string:
            data = j.loads(string)
            return cls.from_dict(data)
        return cls([])
