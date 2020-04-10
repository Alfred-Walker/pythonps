import sys


def solution(n, times):
    answer = sys.maxsize

    max_check_time = max(times)
    start = 1
    end = 1000000000 * 1000000000

    while start <= end:
        mid = start + (end - start) // 2

        checked = 0
        for t in times:
            checked += mid // t

        if checked < n:
            start = mid + 1
        else:
            answer = min(answer, mid)
            end = mid - 1

    return answer


n = 6
times = [7, 10]
print(solution(n, times))
