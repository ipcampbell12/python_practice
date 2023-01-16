my_arr = [-2, 3, 4, 7, 8, 9, 11, 13]


target = 11


def search(arr, targ):
    left = arr[0]
    right = arr[-1]

    middle = len(arr)/2

    for num in arr:
        if num == targ and num > middle:
            middle = left
        elif num == targ and num < middle:
            middle = right

    return middle


print(search(my_arr, target))
