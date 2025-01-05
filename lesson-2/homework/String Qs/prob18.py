def check_edges(text,start,end):
    arr = text.split()
    if arr[0]==start and arr[-1]==end:
        return True
    else:
        return False
    
print(check_edges('Hellow you ugly miserable World', 'Hello', 'World')) # Expected output: True
    