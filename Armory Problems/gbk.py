# GenBank Introduction
from Bio import Entrez

def genCount(s: str) -> int:
    genus, startDate, endDate, _ = s.split("\n")
    Entrez.email = "email@here.com"
    handle = Entrez.esearch(db="nucleotide", term=f'({genus}[Organism]) AND ({startDate}[Publication Date] : {endDate}[Publication Date])')
    record = Entrez.read(handle)

    print(record['Count'])


    
example = """Anthoxanthum
2003/7/25
2005/12/27"""

#genCount(example)

f = open("rosalind_gbk.txt", "r")

genCount(f.read())
