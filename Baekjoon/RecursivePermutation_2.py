# 순열 구현 연습
def permutation(arg_list):
    if len(arg_list) == 0:
        return []
    elif len(arg_list) == 1:
        return [arg_list]
    else:
        ret = []

        for i in range(0, len(arg_list)):
            start = [arg_list[i]]
            new_list = arg_list[:i] + arg_list[i + 1:]

            for p in permutation(new_list):
                ret.append(start + p)

        return ret


print(permutation([0, 1, 2]))
