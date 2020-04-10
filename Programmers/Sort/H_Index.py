def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)

    for i in range(n, -1, -1):
        citated = 0
        # print("i: {0}".format(i))
        for j in range(n):
            if citations[j] >= i:
                 citated += 1

        if citated >= i:
            return i

    return 0


citations = [3, 0, 6, 1, 5]
print(solution(citations))