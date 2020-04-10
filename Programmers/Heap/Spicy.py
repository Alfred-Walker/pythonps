import heapq


def solution(scoville, k):
    answer = 0
    heapq.heapify(scoville)

    while True:
        if len(scoville) == 0:
            answer = -1
            break

        if scoville[0] >= k:
            break

        if len(scoville) == 1:
            answer = -1
            break

        answer += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + second * 2
        heapq.heappush(scoville, new)

    return answer


scoville = [1, 2, 3, 9, 10, 12]
k = 7

print(solution(scoville, k))
