def find_index(arr,item):
    for i in arr:
        if i == item:
            return arr.index(i)
        
arr=[2,4,1,5,12,9,10]
print(find_index(arr,5))