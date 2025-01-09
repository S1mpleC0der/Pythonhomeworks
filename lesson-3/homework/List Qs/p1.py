def find_occurrences(arr,item):
    count=0
    for i in arr:
        if i == item:
            count += 1
    return count