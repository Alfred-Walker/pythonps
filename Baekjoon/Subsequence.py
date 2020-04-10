sub = []


def all_subs(word):
    for i in range(len(word)):
        for j in range(i, len(word)):
            # 연속된 부분문자열 생성
            sb = word[i:j+1]
            if sb not in sub:
                sub.append(sb)

            # 생성한 부분문자열 중 1개를 제거 후 재귀
            for i in range(len(sb)):
                s = sb[0:i] + sb[i + 1: len(sb)]
                if s not in sub:
                    all_subs(s)


all_subs("aabc")
print(sub)
