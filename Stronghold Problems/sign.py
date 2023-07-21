# Enumerating Oriented Gene Orderings

def sign(n):
    """Given: A positive integer n≤7.
    Return: The total number of permutations of length n, followed by a list of all such permutations (in any order)."""
    from itertools import permutations
    nums = range(-int(n), int(n)+1)
    nums = [i for i in nums if i != 0] # drop zero
    perm = permutations(nums, r=int(n))
    values = list(perm)
    for value in values:
        print(sum(map(abs, value)))
        if sum(map(abs, value)) != n:
            values.remove(value) # remove permutations that don't equate to n
    print(f"{len(values)}")
    for item in values:
        print(*item)




example = 2

print(sign(example))

#f = open("rosalind_sign.txt", "r")

#sign(f.read())