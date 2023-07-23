# Conditions and Loops

def oddSum(s: str) -> int:
    """Given: Two positive integers a and b (a<b<10000).
    Return: The sum of all odd integers from a through b, inclusively."""
    a, b = s.split(" ")
    return sum([num for num in range(int(a), int(b)+1) if num%2 != 0])


#print(oddSum("100 200"))


f = open("rosalind_ini4.txt", "r")

print(oddSum(f.read()))