my_arr = [3, 6, 4, 8, 2, 12, 17, 1]


def bubble_sort(arr):

    n = len(arr)

    for k in range(0, n-1):
        flag = 0
        for i in range(0, n-k-1):
            print(arr[i])
            print(arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = 1
        if flag == 0:
            break

    return arr


print(bubble_sort(my_arr))
