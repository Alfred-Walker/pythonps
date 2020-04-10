# 순열 구현 연습
def permutation(arg_list):
    if len(arg_list) == 0:
        return []
    elif len(arg_list) == 1:
        return [arg_list]       # []에 주의
    else:
        ret = []
        for i in range(0, len(arg_list)):
            start = [arg_list[i]]

            list_except_start = arg_list[:i] + arg_list[i+1:]

            # 아직 선택받지 못한 수들로 이루어진 모든 수열들의 조합 앞에 start를 붙임
            for p in permutation(list_except_start):
                ret.append(start + p)

        return ret


print(permutation([1, 2, 3, 4]))
