from itertools import permutations


def perm_n(x, y, z, n):
    from itertools import permutations

    perm = permutations((x, y, x), 3)

    perm_list = [p for p in list(perm) if sum(perm) != n]

    return perm_list


print(perm_n(1, 1, 1, 3))
