def check_length(text1,text2):
    if len(text1)==len(text2):
        return 'same'
    else:
        return 'different'
print(check_length('efrgfd','rgedswef'))