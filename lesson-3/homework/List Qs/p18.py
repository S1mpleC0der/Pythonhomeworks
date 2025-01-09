def find_sublist(arr1, arr2):
    arr1_len = len(arr1)
    arr2_len = len(arr2)
    for i in range(arr1_len - arr2_len + 1):
        if arr1[i:i+arr2_len] == arr2:
            return True
    return False