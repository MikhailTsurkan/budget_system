class RelationMixin:
    child_class = None

    def __init__(self, children, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.children = children

    @classmethod
    def new(cls, *args, **kwargs):
        return cls(children=[], *args, **kwargs)

    def get_or_create(self, _datetime, *args, **kwargs):
        for child in self.children:
            if child.id == child.extract_id(_datetime):
                return child
        return self.create_child(_datetime, *args, **kwargs)

    def create_child(self, _datetime, *args, **kwargs):
        child = self.child_class(_datetime, *args, **kwargs) if not hasattr(self.child_class, "new") else self.child_class.new()
        self.children.append(child)
        return child


class DateTimeIdInit:
    id_field_name = None
    id_field_name_callable = False

    def __init__(self, _datetime, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = self.extract_id(_datetime)

    def extract_id(self, _datetime):
        if isinstance(_datetime, str):
            return _datetime

        _id = getattr(_datetime, self.id_field_name) if self.id_field_name is not None else _datetime
        if self.id_field_name_callable:
            _id = _id()

        if not isinstance(_id, int):
            _id = str(_id)
        return _id
