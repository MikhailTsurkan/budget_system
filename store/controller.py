from datetime import date
import dates


class Controller:
    def __init__(self):
        self.children = []

    def add_notion(self, notion):
        current_date = date.today()
        month_date = current_date.month
        month = self.get_or_create(month_date)


    def create_month(self):
        month = dates.Month()
        self.notions.append(month)
        return month

    def get_or_create(self, month):
        for notion in self.notions:
            if notion.date == month:
                return notion
        return self.create_month()
