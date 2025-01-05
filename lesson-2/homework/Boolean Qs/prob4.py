def check_difference(n1,n2,n3):
    if n1!=n2 and n1!=n3 and n2!=n3:
        return True
    else:
        return False
    
print(check_difference(23,12,44))