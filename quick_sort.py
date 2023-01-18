sort_arr = [-2, 3, -1, 5, 4, -3, 0]


def partition(sort_arr, l, r):
    pivot = sort_arr[r]
    i = l - 1
