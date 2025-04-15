from unittest import result


def power_of_number_recursion(number, power):
    if power <= 0:
        return 1
    if power == 1:
        return number

    return number * power_of_number_recursion(number, power - 1)


def power_of_number_iterative(number, power):
    result = 1
    for i in range(power):
        result *= number

    return result


# Recursion can only call for upto 900
print(power_of_number_recursion(3, 30))

# Iterative can be called infinite times
print(power_of_number_iterative(3, 30))
