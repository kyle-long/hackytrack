class Rename(object):
    def __init__(self, record_reader, command_parts):
        self.command_parts = command_parts
        self.record_reader = record_reader

    def process(self):
        index = int(self.command_parts[0])
        record = self.record_reader.get(index)
        record["name"] = " ".join(self.command_parts[1:])
