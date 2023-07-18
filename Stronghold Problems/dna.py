    # Counting Nucleotides

def ntCounts(s):
    """Given: A DNA string s of length at most 1000 nt.
       Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
    """
    return f"{s.count('A')} {s.count('C')} {s.count('G')} {s.count('T')}"


example = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'

#print(ntCounts(example))

f = open("rosalind_dna.txt", "r")

print(ntCounts(f.read()))