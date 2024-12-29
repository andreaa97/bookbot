import string

path_file = "books/frankenstein.txt"
low_words = []
letters = {}
count_letters = []
n_words = 0
with open(path_file) as f:
    file_contents = f.read()

words = file_contents.split()
n_words = len(words)
for word in words:
    low = ""
    low = word.lower()
    low_words.append(low)

for letter in string.ascii_lowercase:
    letters[letter] = 0

for word in low_words:
    for c in word:
        if c in letters:
            letters[c] += 1

#dict(sorted(letters.items(), key=lambda item: item[1])) sorta per valori
letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
print(f"--- Begin report of {path_file} ---")
print(f"{n_words} words found in the document\n")

for k in letters:
    print(f"The {k} character was found {letters[k]} times")

print("--- End report ---")
#You can use a string's .isalpha() method to check if a string only contains characters from the alphabet.
