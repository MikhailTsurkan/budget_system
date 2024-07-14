class RelationMixin:
    child_class = None

    def __init__(self):
        super().__init__()
        self.children = []

    def get_or_create(self, _datetime, *args):
        for child in self.children:
            if child.id == child.extract_id(_datetime):
                return child
        return self.create_child(_datetime, *args)

    def create_child(self, _datetime, *args):
        child = self.child_class(_datetime, *args)
        self.children.append(child)
        return child


class DateTimeIdInit:
    id_field_name = ""
    id_field_name_callable = False

    def __init__(self, _datetime):
        super().__init__()
        self.id = self.extract_id(_datetime)

    def extract_id(self, _datetime):
        _id = getattr(_datetime, self.id_field_name)
        if self.id_field_name_callable:
            return _id()
        return _id

