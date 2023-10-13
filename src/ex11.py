"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    seconds = tsec % 60
    minutes = (tsec // 60) % 60
    hours = tsec // 3600
    t = ""

    if tsec == 0:
        return "0s"
    if seconds >0:
        t = str(seconds)+"s "
    if minutes >0:
        t = str(minutes)+"m "+ t
    if hours >0:
        t = str(hours)+"h "+ t
    return t.strip()


