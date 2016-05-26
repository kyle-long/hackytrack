import json


class RecordReader(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.record_list = []

    def read(self):
        with open(self.file_name, "r") as f:
            content = f.read().strip()

            if content:
                self.record_list = json.loads(content)

    def last_record(self):
        last = None
        if len(self.record_list):
            last = self.record_list[-1]

        return last

    def add_record(self, record):
        self.record_list.append(record)

    def write(self):
        content = json.dumps(self.record_list)
        with open(self.file_name, "w") as f:
            f.write(content)
