# https://ratsgo.github.io/data%20structure&algorithm/2017/10/16/countingsort/
# digit 은 1, 10, 100...
def counting_sort(arr, digit):
    n = len(arr)

    # 배열의 크기에 맞는 output 배열을 생성하고 10개의 0을 가진 count란 배열을 생성한다.
    output = [0] * n
    count = [0] * 10

    # digit, 자릿수에 맞는 count에 += 1을 한다.
    for i in range(0, n):
        index = int(arr[i] / digit)
        count[index % 10] += 1

    print(count)

    # 기존 count 값을 사용해 count 배열에 count 가 아닌 (중요) 위치값을 저장
    for i in range(1, 10):
        count[i] += count[i - 1]        # count
        print(i, count[i])

    print(count)
    # 앞서 count 에 저장한 위치값을 기반으로 output 에 arr 들을 담는다.
    i = n - 1
    while i >= 0:
        index = int(arr[i] / digit)
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # arr 를 결과물에 다시 재할당한다.
    for i in range(0, n):
        arr[i] = output[i]


# Method to do Radix Sort
def radix_sort(arr):
    # arr 배열중에서 maxValue 를 잡아서 어느 digit, 자릿수까지 반복하면 될지를 정한다.
    max_val = max(arr)
    # 자릿수마다 countingSorting 을 시작한다.
    digit = 1
    while int(max_val / digit) > 0:
        counting_sort(arr, digit)
        digit *= 10


arr = [170, 45, 75, 90, 802, 24, 2, 66]
# arr = [4, 2, 1, 5, 7, 2]
radix_sort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
