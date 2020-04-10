# for loop내의 값 수정 테스트

cnt = [0, 1, 2, 3, 4, 5]

for c in cnt:
    c += 1

print(*cnt)

for i in range(0, len(cnt)):
    cnt[i] += 1

print(*cnt)

# <결과>
# 0 1 2 3 4 5
# 1 2 3 4 5 6
