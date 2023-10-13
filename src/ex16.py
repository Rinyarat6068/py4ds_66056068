"""
Exercise 16
"""


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    if len(num_list) == 0:
        return None

    count = {}

    most_freq_num = None
    most_freq_num_count = 0

    for i in num_list:
        if i not in count:
            count[i] = 0
        count[i] += 1
        if count[i] > most_freq_num_count:
            most_freq_num = i
            most_freq_num_count = count[i]
    return most_freq_num

