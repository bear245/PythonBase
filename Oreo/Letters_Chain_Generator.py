import string
ALLOWED_CHARACTERS = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'D', 'F', 'H', 'J', 'K', 'L', 'X', 'C', 'N', 'M', 3, 4, 7]
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]

def next(string):
    """ Get next sequence of characters.
    Treats characters as numbers (0-255). Function tries to increment
    character at the first position. If it fails, new character is
    added to the back of the list.
    It's basically a number with base = 256.
    :param string: A list of characters (can be empty).
    :type string: list
    :return: Next list of characters in the sequence
    :rettype: list
    """
    if len(string) <= 0:
        string.append(indexToCharacter(0))
    else:
        string[0] = indexToCharacter((characterToIndex(string[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(string[0]) is 0:
            return list(string[0]) + next(string[1:])
    return string

def main():
    sequence = list()
    while True:
        sequence = next(sequence)
        string = ('YN' + )
        print(sequence)

if __name__ == "__main__":
    main()