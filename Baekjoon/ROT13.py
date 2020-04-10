# 문제
# ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
#
# 예를 들어, "Baekjoon Online Judge"를 ROT13으로 암호화하면 "Onrxwbba Bayvar Whqtr"가 된다.
# ROT13으로 암호화한 내용을 원래 내용으로 바꾸려면 암호화한 문자열을 다시 ROT13하면 된다.
# 앞에서 암호화한 문자열 "Onrxwbba Bayvar Whqtr"에 다시 ROT13을 적용하면 "Baekjoon Online Judge"가 된다.
#
# ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다.
# 예를 들어, "One is 1"을 ROT13으로 암호화하면 "Bar vf 1"이 된다.
#
# 문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.
#
# 출력
# 첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.
#
# 예제 입력 1
# Baekjoon Online Judge
# 예제 출력 1
# Onrxwbba Bayvar Whqtr
# 예제 입력 2
# One is 1
# 예제 출력 2
# Bar vf 1

import sys


ord_A = ord('A')
ord_Z = ord('Z')
ord_a = ord('a')
ord_z = ord('z')


def apply_rot13(str_to_encrypt):
    str_encrypted = ""
    for char in str_to_encrypt:
        ord_char = ord(char)
        if ord_A <= ord_char <= ord_Z:
            str_encrypted += chr(ord_A + (ord_char - ord_A + 13) % 26)
        elif ord_a <= ord_char <= ord_z:
            str_encrypted += chr(ord_a + (ord_char - ord_a + 13) % 26)
        else:
            str_encrypted += char

    return str_encrypted


S = sys.stdin.readline().rstrip()
print(apply_rot13(S))
