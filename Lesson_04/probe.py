# Глобальное пространство имен
a, b = 1, 2
print('global:', a+b)


def simple():
    print('simple:', a + b)


simple()