def find_middle(arr):
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2 - 1] + arr[len(arr)//2]) / 2
    else:
        return arr[len(arr)//2]