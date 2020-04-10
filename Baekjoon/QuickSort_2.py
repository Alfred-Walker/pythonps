def partition(li, ri, lis):
    if li >= ri:
        return

    pivot = li
    j = pivot
    for i in range(li + 1, ri + 1):
        if lis[i] < lis[pivot]:
            j += 1
            lis[i], lis[j] = lis[j], lis[i]

    lis[pivot], lis[j] = lis[j], lis[pivot]

    return j


def quick(li, ri, lis):
    if li >= ri:
        return

    pi = partition(li, ri, lis)

    quick(li, pi - 1, lis)
    quick(pi + 1, ri, lis)


test = [0, 1, 5, 3, 4]
quick(0, len(test) - 1, test)
print(test)