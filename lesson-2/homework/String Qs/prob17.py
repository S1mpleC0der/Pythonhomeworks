def replace_vowels(text):
    for i in text:
        if i.lower() in 'aoeiu':
            text = text.replace(i, '*')
    return text

print(replace_vowels('applepiebanana'))