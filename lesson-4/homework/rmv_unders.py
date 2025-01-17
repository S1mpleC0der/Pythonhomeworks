def modify_string(txt):
    vowels = "aeuoi"
    result = []
    for i, char in enumerate(txt):
        result.append(char)
        if (i + 1) % 3 == 0 or char in vowels:
            if i + 1 < len(txt):
                result.append('_')
    return ''.join(result)


