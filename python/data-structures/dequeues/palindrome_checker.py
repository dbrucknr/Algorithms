from deque import Deque

phrase_1 = "madam"
phrase_2 = "racecar"
phrase_3 = "Derek"


def palindrome_checker(phrase):
    deque = Deque()
    for character in phrase:
        deque.add_rear(character)

    while deque.size() != 0:
        if deque.peek_front() == deque.peek_rear():
            deque.remove_front() and deque.remove_rear()
        else:
            break

    return deque.size() == 0


print(palindrome_checker(phrase_1))
print(palindrome_checker(phrase_3))
print(palindrome_checker(phrase_2))


def palindrome_checker_alternate(phrase):
    deque = Deque()
    for character in phrase:
        deque.add_rear(character)

    while deque.size() >= 2:
        front = deque.remove_front()
        rear = deque.remove_rear()

        if front != rear:
            return False
    return True
