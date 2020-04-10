# 다솜이는 자기 방 번호를 플라스틱 숫자로 문에 붙이려고 한다.
# 플라스틱 숫자 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다.
# 다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최솟값을 출력하시오.
# (6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

# 입력: 첫째 줄에 다솜이의 방 번호 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.
# 출력: 첫째 줄에 필요한 세트의 개수를 출력한다.

import sys


N = int(sys.stdin.readline().rstrip())
numbers = [0] * 10
set_cnt = 0

if N == 0:
    set_cnt = 1
else:
    while N != 0:
        last_digit = N % 10
        if numbers[last_digit] == 0:
            if last_digit == 6 and numbers[9] != 0:
                numbers[9] -= 1
            elif last_digit == 9 and numbers[6] != 0:
                numbers[6] -= 1
            else:
                for i in range(0, 10):
                    numbers[i] += 1
                numbers[last_digit] -= 1
                set_cnt += 1
        else:
            numbers[last_digit] -= 1

        N = int(N * 0.1)

print(set_cnt)
