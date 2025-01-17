def uncommon_elements(list1, list2):
    from collections import Counter
    counter1 = Counter(list1)
    counter2 = Counter(list2)
    
    uncommon = []
    for key in counter1.keys() ^ counter2.keys():
        uncommon.extend([key] * (counter1[key] + counter2[key]))
    for key in counter1.keys() & counter2.keys():
        if counter1[key] != counter2[key]:
            uncommon.extend([key] * abs(counter1[key] - counter2[key]))
    
    return uncommon


