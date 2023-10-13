"""
Execise 6
"""


def ordinal_suffix(num):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # FIX : complete this
    if num == 0 or num >= 4 and num <= 100:
        return str(num)+"th"
    elif num == 1 or num == 101:
        return str(num)+"st"
    elif num == 2:
        return str(num)+"nd"
    elif num == 3:
        return str(num)+"rd"
    else:
        return "error"
