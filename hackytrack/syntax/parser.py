from hackytrack.syntax.rename import Rename


class Parser(object):
    def __init__(self, record_reader):
        self.record_reader = record_reader

    def find_command(self, line):
        line = line.strip()
        command = None
        if line[0] == "/":
            removed_special_character = line[1:]
            command_parts = removed_special_character.split(" ")
            command = self._determine_command(command_parts)

        return command

    def _determine_command(self, command_parts):
        command = command_parts[0]
        command_parts = command_parts[1:]
        if command == "rename":
            return Rename(self.record_reader, command_parts)
