# c=
# c-
# dz=
# d-
# lj
# nj
# s=
# z=

# dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다.
# 위 목록에 없는 알파벳은 한 글자씩 센다.

# 입력: 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
# 단어는 크로아티아 알파벳으로 이루어져 있다.
# 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.

# 출력: 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
import sys


def get_croatian_count(_alphabet):
    dz_count = _alphabet.count("dz=")
    lj_count = _alphabet.count("lj")
    nj_count = _alphabet.count("nj")
    eq_count = _alphabet.count("=")
    hyphen_count = _alphabet.count("-")
    return len(_alphabet) - eq_count - dz_count - lj_count - nj_count - hyphen_count


word = sys.stdin.readline().rstrip()
print(get_croatian_count(word))
