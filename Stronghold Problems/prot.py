# Translating RNA into protein

def rnaProt(s: str) -> str:
    """Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
    Return: The protein string encoded by s."""
    return prots(codons(s))


def codons(mrna: str) -> list:
    """Break up mRNA into codons"""
    return [mrna[i:i+3] for i in range(0, len(mrna), 3)]

def prots(codon: list) -> list:
    """Convert RNA to protein."""
    match codon:
        case "UUU" | "UUC":
            return "F"
        case "UUA" | "UUG" | "CUU" | "CUC" | "CUA" | "CUG":
            return "L"
        case "UCU" | "UCC" | "UCA" | "UCG" | "AGU" | "AGC":
            return "S"
        case "UAU" | "UAC":
            return "Y"
        case "UGU" | "UGC":
            return "C"
        case "UGG":
            return "W"
        case "CCU" | "CCC" | "CCA" | "CCG":
            return "P"
        case "CAU" | "CAC":
            return "H"
        case "CAA" | "CAG":
            return "Q"
        case "CGU" | "CGC" | "CGA" | "CGG" | "AGA" | "AGG":
            return "R"
        case "AUU" | "AUC" | "AUA":
            return "I"
        case "AUG":
            return "M"
        case "ACU" | "ACC" | "ACA" | "ACG":
            return "T"
        case "AAU" | "AAC":
            return "N"
        case "AAA" | "AAG":
            return "K"
        case "GUU" | "GUC" | "GUA" | "GUG":
            return "V"
        case "GCU" | "GCC" | "GCA" | "GCG":
            return "A"
        case "GAU" | "GAC":
            return "D"
        case "GAA" | "GAG":
            return "E"
        case "GGU" | "GGC" | "GGA" | "GGG":
            return "G"
        case "UAA" | "UAG" | "UGA":
            pass
        case _:
            pass


def translation(mrna):
    result = [prots(i) for i in mrna]
    return ''.join([str(elem) for elem in result])

example = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"


#print(translation(codons(example)))

f = open("rosalind_prot.txt", "r")

print(translation(codons(f.read()))) # Results in two "None" results at the end...