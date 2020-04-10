# https://jay-ji.tistory.com/33

# An = {a0, a1, a2, ...an}
# Bn = {b0, b1, b2, ...b,}

def lcs_subsequence(n_list, input_name):
    for compare_name in n_list:
        LCS = [[0] * (len(compare_name) + 1) for i in range(len(input_name) + 1)]
        ans = 0
        for i in range(1, len(input_name) + 1):
            for j in range(1, len(compare_name) + 1):
                if input_name[i - 1] == compare_name[j - 1]:
                    LCS[i][j] = LCS[i - 1][j - 1] + 1
                else:
                    LCS[i][j] = max([LCS[i][j - 1], LCS[i - 1][j]])

        print("- {}와 {}\n  매칭 길이 = {}".format(
            compare_name, input_name, LCS[len(input_name)][len(compare_name)])
        )

        i = len(input_name)
        j = len(compare_name)
        matched_str = ""
        # 매칭되는 글자 출력            <== 연속된 문자열이 아니므로 슬라이싱 처리 불가
        while i != 0 and j != 0:
            if LCS[i - 1][j] < LCS[i][j] and LCS[i][j - 1] < LCS[i][j]:
                matched_str += input_name[i - 1]
                i -= 1
                j -= 1
            elif LCS[i - 1][j] < LCS[i][j]:
                j -= 1
            elif LCS[i][j - 1] < LCS[i][j]:
                i -= 1
            else:  # 같은 경우
                i -= 1
                j -= 1

        matched_str = "".join(reversed(matched_str))
        print("  매칭 문자열 : {}\n".format(matched_str))


if __name__ == "__main__":
    name_list = ['jay', 'ferrnanodo', 'jake', 'jejajeji', 'jqqqaeeeyyji']

    input = 'jayji'

    # Longest Common Substring
    # lcs_substring(name_list, input)

    # print('\n\n\n')

    # Longest Common Subsequence
    lcs_subsequence(name_list, input)
