def add(*args):
    return sum(args)


def add_1(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4 ,5, 6))
print(add_1(1, 5, 4, 9, 0))


def calculate(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)


calculate(add="+", multiply="*", divide="/")