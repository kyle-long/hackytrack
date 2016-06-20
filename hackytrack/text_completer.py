import readline


class TextCompleter(object):
    """
        Deals with tab completion from history file.
    """
    HISTORY_FILE = ".hacky.hist"

    def __init__(self):
        readline.read_history_file(TextCompleter.HISTORY_FILE)
        # limiting to 1000 entries.
        readline.set_history_length(1000)

    def complete(self, text, state):
        """
            Deals with tab completion.

            Args:
                text(string)
                state(int)
            Returns:
                string | None
        """
        response = None
        history = self.get_history()
        matches = []

        if text:
            matches = sorted(s for s in history if s and s.startswith(text))

        try:
            response = matches[state]
        except IndexError:
            response = None

        return response

    def get_history(self):
        """
            Gets history from hacky.hist file.

            Returns:
                list
        """
        history = []

        for i in xrange(1, readline.get_current_history_length() + 1):
            history.append(readline.get_history_item(i))

        return history
