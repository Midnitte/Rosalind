# Dictionaries

def wordNums(s: str) -> dict:
    """Given: A string s of length at most 10000 letters.
    Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order."""
    wordsCount = {}
    for word in s.strip("\n").split(' '):
        wordsCount[word] = wordsCount.setdefault(word, 0) + 1
    for word in wordsCount:
        print(f"{word} {wordsCount[word]}")


example = "We tried list and we tried dicts also we tried Zen"

#wordNums(example)


f = open("rosalind_ini6.txt", "r")

wordNums(f.read())