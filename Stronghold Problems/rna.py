# Transcribing DNA to RNA

def transRNA(t: str) -> str:
    """Given: A DNA string t having length at most 1000 nt.
    Return: The transcribed RNA string of t."""
    translated = t.maketrans("ATGC", "AUGC")
    return t.translate(translated)


example = "GATGGAACTTGACTACGTAAATT"

#print(transRNA(example))

f = open("rosalind_rna.txt", "r")

print(transRNA(f.read()))
