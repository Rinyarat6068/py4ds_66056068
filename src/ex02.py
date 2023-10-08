"""
Execise 2
"""


def convert_to_fahrenheit(celcius=0):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    # FIX : complete this
    return (9/5) * celcius +32


def convert_to_celsius(fahrenheit=0):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    - float: The temperature in Celsius.
    """
    # FIX : complete this
    return (fahrenheit - 32) * (5/9)