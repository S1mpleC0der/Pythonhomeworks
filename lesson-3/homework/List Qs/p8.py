def slice_list(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i])
        if i == 2:
            break
    return new_arr

