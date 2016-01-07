from string import ascii_letters


def search_phone(param):
    final_number = ''

    for c in param:
        if c in ascii_letters:
            final_number += letter_to_number(c)
        else:
            final_number += c

    return final_number


def letter_to_number(char):
    dict_ = {
        '2': ('A', 'B', 'C'),
        '3': ('D', 'E', 'F'),
        '4': ('G', 'H', 'I'),
        '5': ('J', 'J', 'L'),
        '6': ('M', 'N', 'O'),
        '7': ('P', 'Q', 'R', 'S'),
        '8': ('T', 'U', 'V'),
        '9': ('W', 'X', 'Y', 'Z'),
    }
    return [n for n in dict_.keys() if char.upper() in dict_[n]][0]