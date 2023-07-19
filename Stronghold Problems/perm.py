# Enumerating Gene Orders

def perm(n):
    """Given: A positive integer n≤7.
    Return: The total number of permutations of length n, followed by a list of all such permutations (in any order)."""
    from itertools import permutations
    nums = range(1, int(n)+1)
    perm = permutations(nums)
    values = list(perm)
    print(f"{len(values)}")
    for i in values:
        print(*i)

example = 3

#print(perm(example))

f = open("rosalind_perm.txt", "r")

perm(f.read())