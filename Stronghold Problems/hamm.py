# Counting Point Mutations

def pointMut(s:str, t:str) -> int:
    """Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t)."""
    count = 0
    for x, _ in enumerate(s):
        if s[x] != t[x]:
            count = count + 1
    return count

#print(pointMut("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))

f = open("rosalind_hamm.txt", "r")
s, t = f.read().split()

print(pointMut(s, t))
