text = input('enter: ')
flag = False
for i in text:
    if i.isdigit():
        flag = True
        break
    
print(flag)
        