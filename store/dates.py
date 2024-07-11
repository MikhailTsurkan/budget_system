import json as j
from datetime import date
from store.notions import Notion


class Date:

    def json(self, dumped=True):
        serialized = []
        for child in self.children:
            serialized.append(child.json(dumped=False))
        data = {"date": str(self.id), "operations": serialized}
        return j.dumps(data) if dumped else data

    def create_file(self):
        with open(f"{self.__class__.__name__.lower()}-{self.id}", "w") as f:
            f.write(self.json())


class Day(Date):
    child_class = Notion

    def __init__(self):
        super().__init__()
        self.id = date.today().day


class Month(Date):
    child_class = Day

    def __init__(self):
        super().__init__()
        self.date = date.today().month
