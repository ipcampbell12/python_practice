

my_arr = [-2, 3, 4, 7, 8, 9, 11, 13]


target = 11


def search(arr, targ):
    left = 0
    right = len(arr)-1

    while left <= right:
        middle = (len(arr)//2)
        if arr[middle] == targ:
            return middle
        elif targ < arr[middle]:
            right = middle - 1
        elif targ > arr[middle]:
            left = middle + 1
# don't include middle, that's why + 1 or -1
    return -1


print(search(my_arr, target))
