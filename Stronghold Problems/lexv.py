# Ordering Strings of Varying Length Lexicographically
from pprint import pprint
def lexv(s: str) -> str:
    """Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4). 
    Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)"""
    from itertools import permutations
    order = {b: a for a, b in enumerate(set(s.split(" ")))}
    print(order)
    perms = []
    for perm in range(1, len(s)):
        perms.append(set((permutations(s, r=perm))))
        pprint(set((permutations(s, r=perm))))
    return list(perms).sort(key=order[1])


example = "D N A"

solution = str(lexv(example))

pprint(solution)

with open('lexv_solve.txt', 'w') as file:
    file.write(solution)

