from collections import deque
import sys


def get_max_disc_size(rods, rod_index):
    if len(rods[rod_index]) == 0:
        return sys.maxsize
    else:
        return rods[rod_index][-1]


def hanoi_iterative(num):
    whole_moves = []
    rod = dict()
    rod[0] = deque()  # from
    rod[1] = deque()  # aux
    rod[2] = deque()  # to

    for i in range(num):
        rod[0].append(num - i)

    prev_rod = [2, 0, 1]
    next_rod = [1, 2, 0]
    min_rod = 0
    is_turn_to_move_min_rod = True
    total_move = 2 ** num - 1

    if num % 2 == 0:
        min_rod_dir = 1
    else:
        min_rod_dir = -1



    for i in range(total_move):
        if is_turn_to_move_min_rod:
            old_rod = min_rod
            min_rod = (min_rod + min_rod_dir + 3) % 3       # -1 % 3 방지
            whole_moves.append("{0} => {1}".format(old_rod, min_rod))
            rod[min_rod].append(rod[old_rod].pop())
        else:
            if get_max_disc_size(rod, prev_rod[min_rod]) > get_max_disc_size(rod, next_rod[min_rod]):
                whole_moves.append("{0} => {1}".format(next_rod[min_rod], prev_rod[min_rod]))
                rod[prev_rod[min_rod]].append(rod[next_rod[min_rod]].pop())
            else:
                whole_moves.append("{0} => {1}".format(prev_rod[min_rod], next_rod[min_rod]))
                rod[next_rod[min_rod]].append(rod[prev_rod[min_rod]].pop())

        is_turn_to_move_min_rod = not is_turn_to_move_min_rod

    return whole_moves


N = int(sys.stdin.readline().rstrip())
print(hanoi_iterative(N))
