N = 10  # 수열의 크기
sub_sum = 56   # count 할 부분합
A = [13, 44, 42, 3, 55, 1, 55]

left = right = total = answer = 0


while True:
    if total <= sub_sum:
        # 부분합이 M보다 작거나 같은 경우
        if right == N:  # 중요
            break
        total += A[right]
        right += 1
    else:
        # 부분합이 M보다 큰 경우
        total -= A[left]
        left += 1

    # 제일 앞에 와도 무관
    if total == sub_sum:
        answer += 1

print(answer)


