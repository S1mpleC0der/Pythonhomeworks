text = input('enter: ')
separator = input('enter: ')

words = text.split()
new_words = separator.join(words)
print(new_words)