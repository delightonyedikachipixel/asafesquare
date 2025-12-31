def add_ing(word):
    if len(word) < 3:
        return word
    elif word.endswith("ing"):
        return word + "ly"
    else:
        return word + "ing"


x = input("Enter a string: ")
result = add_ing(x)
print(result)

