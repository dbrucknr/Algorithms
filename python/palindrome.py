from reverse_array import reverse_array


def palindrome(string):
    if string == string[::-1]:
        return True
    return False


print(palindrome("madam"))
print(palindrome("racecar"))


# Linear run time complexity
def is_palindrome(string):
    reversed_string = reverse_array(list(string))

    if "".join(reversed_string) == string:
        return True
    return False


print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("radar"))
