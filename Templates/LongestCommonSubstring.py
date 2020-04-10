# https://twinw.tistory.com/126
# https://sssunho.tistory.com/14
# https://only2sea.wordpress.com/2012/10/02/%EC%B5%9C%EC%9E%A5-%EA%B3%B5%ED%86%B5-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4/


def _extractLCS(self, target, comparison_target):
    # Longest Common Substring(LCS)를 이용하여 검색한 문장을 검색된 내용과 일치하는 부분을 찾는다.
    # :param target: A, 검색할 문장
    # :param comparison_target: B, 비교 대상
    # :return: 일치하는 부분. B에서 A와 일치하는 부분
    len_t = len(target)
    len_c = len(comparison_target)
    result = ''

    for i in range(len_t):
        for j in range(len_c):
            lcs_temp = 0
            match = ''

            # i + lcs_temp 는 target 길이 보다 작아야함
            # j + lcs_temp 는 comparison_target 길이 보다 작아야함
            # 위의 두 인덱스 범위 조건을 만족시키면서 동일한 문자가 나올 때마다 lcs_temp 갱신
            while (i + lcs_temp < len_t) and (j + lcs_temp < len_c) and (target[i + lcs_temp] == comparison_target[j + lcs_temp]):
                match += comparison_target[j + lcs_temp]
                lcs_temp += 1

                if len(match) > len(result):
                    result = match

    return result


def LongestCommonSequence(a, b):
    width = len(a) + 1
    height = len(b) + 1
    table = [""] * (width * height)

    def GetTable(r, c):
        return table[r * width + c]

    def SetTable(r, c, value):
        table[r * width + c] = value

    for b_len in range(1, height):
        for a_len in range(1, width):
            if a[a_len-1] == b[b_len-1]:
                SetTable(b_len, a_len, GetTable(b_len - 1, a_len - 1) + a[a_len-1])
                continue
            a_lcs, b_lcs = GetTable(b_len - 1, a_len), GetTable(b_len, a_len - 1)

            if len(a_lcs) > len(b_lcs):
                SetTable(b_len, a_len, a_lcs)
            else:
                SetTable(b_len, a_len, b_lcs)

    return GetTable(height - 1, width - 1)


# print LongestCommonSequence("ABCFAEF", "BACFE")