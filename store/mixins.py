class RelationMixin:
    child_class = None

    def __init__(self):
        super().__init__()
        self.children = []

    def get_or_create(self, id):
        for child in self.children:
            if child.id == id:
                return child
        return self.create_child()

    def create_child(self):
        child = self.child_class()
        self.children.append(child)
        return child

    def add_child(self, child):
        self.children.append(child)
