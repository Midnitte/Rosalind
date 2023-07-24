# Introduction to the Bioinformatics Armory

from Bio.Seq import Seq

def baseCount(s: str) -> str:
    """"""
    aSeq = Seq(s)
    print(aSeq.count('A'), aSeq.count('C'), aSeq.count('G'), aSeq.count('T'))


my_seq = Seq("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")

#baseCount(my_seq)

f = open("rosalind_ini.txt", "r")

baseCount(f.read())