def count_odd(arr):
    count = 0
    for i in arr:
        if i % 2 != 0:
            count += 1
    return count