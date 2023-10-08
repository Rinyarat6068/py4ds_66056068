"""
Execise 2
"""


def convert_to_fahrenheit(Celcius=0):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    # FIX : complete this
    return (9/5) * Celcius +32


def convert_to_celsius(Fahrenheit=0):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    - float: The temperature in Celsius.
    """
    # FIX : complete this
    return (Fahrenheit - 32) * (5/9)