from itertools import chain, product
ALLOWED_CHARACTERS = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'P', 'A', 'D', 'F', 'H', 'J', 'K', 'L', 'X', 'C', 'N', 'M', '3', '4', '7']
TEST_CHARS = ['Q', 'W', 'E', 'R', 'T', 'Y']
def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

# Open external txt file and write "info" into it. Close will perform automatically
# codesFile = open('C:\\Users\\Oleksandr Siora\\PycharmProjects\\PythonBase\\Oreo\\codes.txt')  # Open file in ReadMode

Complete = list(bruteforce(ALLOWED_CHARACTERS, 5))
for i in range(len(Complete)):
    # print(Complete[i])
    CODE = 'YNH' + Complete[i]
    if len(CODE)>7:
        with open('somefile2.txt', 'a') as the_file:
            the_file.write(CODE + '\n')
    print(CODE)

print(len(Complete))