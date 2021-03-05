from itertools import chain, product
ALLOWED_CHARACTERS = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'D', 'F', 'H', 'J', 'K', 'L', 'X', 'C', 'N', 'M', '3', '4', '7']
TEST_CHARS = ['Q', 'W', 'E', 'R', 'T', 'Y']
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

Complete = list(bruteforce(ALLOWED_CHARACTERS, 5))
print(Complete)
print(len(Complete))