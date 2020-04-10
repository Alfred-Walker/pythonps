import sys


def set_pos(rect):
    rect = rect.split('\n')
    new_rect = []
    n = len(rect)
    chunk = ' ' * n

    # Top
    for line in rect:
        new_rect.append(line * 3)

    # Mid
    for line in rect:
        new_rect.append(line + chunk + line)

    # Bottom
    for line in rect:
        new_rect.append(line * 3)

    return '\n'.join(new_rect)


def draw_rect(arg_pow):
    if arg_pow == 0:
        return '*'

    return set_pos(draw_rect(arg_pow - 1))


N = int(sys.stdin.readline().rstrip())
pool = [3**i for i in range(0, 8)]
power = pool.index(N)
print(draw_rect(power))
