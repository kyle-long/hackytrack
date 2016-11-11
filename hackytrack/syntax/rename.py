class Rename(object):
    def __init__(self, record_reader, command_parts):
        self.command_parts = command_parts
        self.record_reader = record_reader

    def process(self):
        try:
            index = int(self.command_parts[0])
            if index < 1:
                raise ValueError("Index must be 1 or greater")

            record = self.record_reader.get(index)

            new_name = " ".join(self.command_parts[1:])

            if not new_name:
                raise ValueError("Did not provide name")

            record["name"] = new_name
        except ValueError as err:
            print "The rename command requires you enter first an interger (to specify which record you wish to alter) and the name you wish to rename it to."
            print "Error: {0}".format(err.message)
