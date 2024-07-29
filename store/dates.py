import json as j
from datetime import date
from store.notions import Notion
from store.mixins import DateTimeIdInit, RelationMixin
import os


class Date(DateTimeIdInit, RelationMixin):
    def json(self, dumped=True):
        to_save = []
        for child in self.children:
            to_save.append(child.json(dumped=False))
        to_save_dict = self.__dict__.copy()
        to_save_dict["children"] = to_save
        return j.dumps(to_save_dict) if dumped else to_save_dict

    def create_file(self, dirname):
        path = os.path.join(dirname, f"{self.__class__.__name__.lower()}-{self.id}")
        with open(path, "w") as f:
            f.write(self.json())

    def from_file(cls, path):
        with open(path) as f:
            data = j.load(f)

        children = data.pop("children")

        obj = cls
