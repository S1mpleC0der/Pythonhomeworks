def min(arr):
    min_val = arr[0]
    for i in range(1,len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val