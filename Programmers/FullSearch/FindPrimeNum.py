from itertools import permutations


def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    prime_numbers = []
    answer = 0

    # 길이 1 이상 7 이하
    for i in range(1, len(numbers) + 1):
        # 2개의 원소로 수열 만들기
        permu = list(map(''.join, permutations(numbers, i)))

        for p in permu:
            p = int(p)
            if is_prime(p) and p not in prime_numbers:
                prime_numbers.append(p)

    answer = len(prime_numbers)

    return answer


numbers = "011"
print(solution(numbers))
