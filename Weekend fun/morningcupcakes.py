word= input("Enter a word:")
vowel_count = 0
consonant_count = 0
word_count = len(word)
for counter in word.upper():

    if (counter == "A" or counter == "E" or counter=="I" or  counter == "O" or counter == "U"):
        vowel_count += 1
    else:
        consonant_count += 1
print(f" Total number of words: {word_count} ")
print(f"Total Vowels: {vowel_count}")
print(f"Total Consonants: {consonant_count}")
