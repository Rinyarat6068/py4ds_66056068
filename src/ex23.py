"""
Exercise 23 : 99 Bottles of Beer on the Wall
"""


def bottles_of_beer(beer):
    """
    Calculate the number of bottles of beer on the wall.
    And print out like this :

    99 bottles of beer on the wall,
    99 bottles of beer.
    Take one down, pass it around,
    98 bottles of beer on the wall.
    ...
    1 bottle of beer on the wall,
    1 bottle of beer.
    Take one down, pass it around,
    No more bottles of beer on the wall!

    Returns:
        str: The repeated lyrics of bottles of beer on the wall.
    """
    # FIX : complete this
    result = ''
    if beer != 1:
        result += str(beer) + ' bottles of beer on the wall,\n'
        result += str(beer) + ' bottles of beer.\n'
        result += 'Take one down, pass it around,\n'
        if (beer - 1) == 1:
            result += '1 bottle of beer on the wall.\n'
        else:
            result += str(beer - 1) + ' bottles of beer on the wall.\n'
    else:
        result += '1 bottle of beer on the wall,\n'
        result += '1 bottle of beer.\n'
        result += 'Take one down, pass it around,\n'
        result += 'No more bottles of beer on the wall!\n'
    return result

def loop_bottles_of_bears(bottle):
    while bottle > 0:
        print(bottles_of_beer(bottle))
        bottle -= 1


if __name__ == '__main__':
    loop_bottles_of_bears(5)
