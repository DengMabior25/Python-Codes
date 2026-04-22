text = "mang kasir aplikasi sederhana"
words = 0
characters = 0
is_in_word = False

for char in text:
    if char != " ":
        characters += 1
        if not is_in_word:
            words += 1
            is_in_word = True
        else:
            is_in_word = False
    print(words)
    print(characters)