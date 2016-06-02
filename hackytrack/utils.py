import datetime


def get_today():
    """
        Get current day formatted string.

        Returns:
            string: date formatted '%Y-%m-%d'
    """
    date = datetime.datetime.now()
    today = date.strftime("%Y-%m-%d")

    return today
