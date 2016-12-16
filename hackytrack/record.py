import re
import datetime


class Record(object):
    def __init__(self, name, delta=None):
        # Full original name
        self.name = name
        if delta is None:
            delta = datetime.timedelta()

        self.delta = delta
        self.record_list = []

    @property
    def description(self):
        description = re.sub(".*?:", "", self.name, 1).strip()
        return description

    @property
    def total(self):
        return self.delta

    def add(self, record):
        self.delta = self.delta + record.delta
