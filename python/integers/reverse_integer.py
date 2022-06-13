
def reverse_integer(number) -> int:
    reversed_number = 0
    remainder = 0

    while number > 0:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder
        number = number // 10

    return reversed_number


print(reverse_integer(1234))
