# Enumerating k-mers Lexicographically
from itertools import permutations

def lexi(alpha, n):
    """Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).
    Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet)."""
    alpha = alpha+alpha
    alpha = list(alpha.replace(' ', ''))

    perms = permutations(alpha, n)

    results = sorted(list(set(perms)))
    for result in results:
        print("".join([i for i in result]))


alpEx = "A C G T"

numEx = 2

#print(lexi(alpEx, numEx))

f = open("rosalind_lexf.txt", "r")
alphaBet, nums, _ = f.read().split('\n')
lexi(alphaBet, int(nums))
