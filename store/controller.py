from datetime import datetime
import dates
from store.mixins import RelationMixin
from store.notions import Notion


class Controller(RelationMixin):
    child_class = dates.Month
    target_class = Notion

    def create_target(self, *args, **kwargs):
        current_datetime = datetime.now()

        parent = self
        while hasattr(parent, "get_or_create"):
            child = parent.get_or_create(current_datetime)
            parent = child

        parent.__init__(*args, **kwargs)
        return parent
