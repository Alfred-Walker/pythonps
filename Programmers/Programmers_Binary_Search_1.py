def solution(budgets, M):
    answer = 0
    min_share = 1
    max_share = 100000

    while min_share <= max_share:
        temp_share_sum = 0
        mid_share = (min_share + max_share) >> 1

        for b in budgets:
            temp_share_sum += min(b, mid_share)

        if temp_share_sum <= M and mid_share <= max(budgets):   # budgets 의 최대값 넘길 수 없음에 주의
            answer = max(answer, mid_share)
            min_share = mid_share + 1
        else:
            max_share = mid_share - 1

    return answer


b = [120, 110, 140, 150]
M = 485

print(solution(b, M))
