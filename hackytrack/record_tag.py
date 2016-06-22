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
            existing = self._find_existing_item(name, combined_list)
            if existing:
                existing["delta"] += item["delta"]
            else:
                combined_list.append(item)

        return combined_list

    def add_item(self, item):
        self.item_list.append(item)

    def _find_existing_item(self, name, combined_list):
        for item in combined_list:
            if name == item["name"]:
                return item

        return None
