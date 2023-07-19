# Complementing a strand of DNA

def compDNA(s: str) -> str:
    """Given: A DNA string s of length at most 1000 bp.
    Return: The reverse complement sc of s."""
    
    translated = s[::-1].maketrans("ATCG", "TAGC")
    return s[::-1].translate(translated)


example = "AAAACCCGGT"


#print(compDNA(example))

f = open("rosalind_revc(1).txt", "r")

print(compDNA(f.read()))

