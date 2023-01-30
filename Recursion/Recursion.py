a = 5


def su(x):
    if x == 1:
        return 1

    return x+sum(x-1)


print(su(a))
