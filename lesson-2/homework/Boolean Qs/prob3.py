def pos_or_even(num):
    if num>0:
        if num%2==0:
            return 'even and positive'
        else:
            return 'odd and positive'
    else:
        return 'negative'
    
print(pos_or_even(-55))