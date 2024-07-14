import json as j
from datetime import date
from store.notions import Notion
from store.mixins import DateTimeIdInit, RelationMixin


class Date(DateTimeIdInit, RelationMixin):
    def create_file(self):
        with open(f"{self.__class__.__name__.lower()}-{self.id}", "w") as f:
            f.write(self.json())


class Day(Date):
    child_class = Notion
    id_field_name = "day"


class Month(Date):
    child_class = Day
    id_field_name = "month"
