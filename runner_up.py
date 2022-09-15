
# need to find the second highest value

def runner_up(arr):
    arr_sort = sorted(list(set(arr,)), reverse=True)
    return arr_sort[1]


print(runner_up([2, 3, 6, 6, 5]))
