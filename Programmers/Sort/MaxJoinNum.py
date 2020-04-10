# https://www.geeksforgeeks.org/python-largest-number-possible-from-list-of-given-numbers/
from functools import cmp_to_key


def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key=cmp_to_key(lambda i, j: -1 if str(j) + str(i) < str(i) + str(j) else 1))
    answer = "".join(numbers)

    return answer


numbers = [1004, 14, 14, 12, 9]
numbers = [3, 30, 34, 5, 9]

print(solution(numbers))
