import os
codesFile = open('C:\\Users\\Oleksandr Siora\\PycharmProjects\\PythonBase\\Oreo\\codes.txt') #Open file in ReadMode
listFile = codesFile.readlines()
print(listFile)
print(listFile[1])
codesFile.close()

# print(os.path.abspath('codes.txt'))