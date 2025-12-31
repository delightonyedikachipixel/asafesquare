def longest_word(words):
    word_list = words.split()
    longest = max(word_list, key=len)
    return f"{longest}.{len(longest)}"


x = input("Enter a list of words: ")
result = longest_word(x)
print(result)

