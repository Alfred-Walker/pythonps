def num_to_base(n, b):
    convert = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if n == 0:
        return 0

    digits = ['0']

    while n:
        to_append = int(n % b)
        digits.append(convert[to_append])
        n //= b

    # 역순을 리턴
    return digits[::-1]

