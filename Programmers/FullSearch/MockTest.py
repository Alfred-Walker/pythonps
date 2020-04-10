def solution(answers):
    answer = []

    a = [i % 5 + 1 for i in range(len(answers))]

    b_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    b = [b_pattern[i % 8] for i in range(len(answers))]

    c_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c = [c_pattern[i % 10] for i in range(len(answers))]

    cnt_1 = cnt_2 = cnt_3 = 0
    max_cnt = 0

    for i in range(len(answers)):
        if a[i] == answers[i]:
            cnt_1 += 1

        if b[i] == answers[i]:
            cnt_2 += 1

        if c[i] == answers[i]:
            cnt_3 += 1

    max_cnt = max(cnt_1, cnt_2, cnt_3)

    if max_cnt == cnt_1:
        answer.append(1)

    if max_cnt == cnt_2:
        answer.append(2)

    if max_cnt == cnt_3:
        answer.append(3)

    return answer


answers = [3, 3, 3, 4, 5, 1, 3, 3, 3, 4, 5, 1, 3, 3, 3, 4, 5, 1]
print(solution(answers))
