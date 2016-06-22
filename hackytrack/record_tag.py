import datetime


class RecordTag(object):
    def __init__(self, name):
        self.item_list = []
        self.name = name

    @property
    def total(self):
        total = datetime.timedelta()
        for item in self.item_list:
            total += item["delta"]

        return total

    @property
    def combined_item_list(self):
        combined_list = []

        for item in self.item_list:
            name = item["name"]
            if name not in combined_list:
                combined_list[name] = item
            else:
                combined_list[name]["elapsed"] += item["elapsed"]

        return combined_list

    def add_item(self, item):
        self.item_list.append(item)
