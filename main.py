import string

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
#print(len(words))
low_words = []
letters = {}
for word in words:
    low = ""
    low = word.lower()
    low_words.append(low)


for letter in string.printable:
    letters[letter] = 0
    
for word in low_words:
    for c in word:
        letters[c] += 1

print(letters)