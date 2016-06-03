import readline


class TextCompleter(object):
    """
        Deals with tab completion from history file.
    """
    HISTORY_FILE = ".hacky.hist"

    def __init__(self):
        self.matches = []

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

        if state == 0:
            if text:
                self.matches = [s for s in history if s and s.startswith(text)]
            else:
                self.matches = self.options[:]

            try:
                response = self.matches[state]
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
