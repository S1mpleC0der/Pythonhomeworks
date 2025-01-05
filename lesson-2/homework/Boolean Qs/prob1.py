def check_empty(name,password):
    if not name and not password:
        return False
    else:
        return True
    
print(check_empty('',''))
        