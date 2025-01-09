def filter_odds(arr):
    filtered=[]
    for i in arr:
        if i%2!=0:
            filtered.append(i)
            
    return filtered
