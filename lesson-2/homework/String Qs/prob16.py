def remove_char(text,char):
    for i in text:
        if i == char:
            text = text.replace(i, '')
    return text

print(remove_char('applepiebanana','a'))