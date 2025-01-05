def replace_word(text, word, new_word):
    if word in text:
        return text.replace(word, new_word)
    
print(replace_word('Hello World', 'World', 'Universe'))