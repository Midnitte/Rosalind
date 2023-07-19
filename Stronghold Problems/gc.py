#
import pprint
import re

regex = re.compile('>(?P<ID>Rosalind_\d{4})\n(?P<SEQ>(\w*\n{0,1})*)')


def gcContent(s: str) -> str:
    """Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
    Return: The ID of the string having the highest GC-content, followed by the GC-content of that string."""
    def gcCalc(x: str) -> float:
        return sum(map(x.count, ['C','G']))/len(x)*100
    strings = regex.findall(s)
    return strings


example =""">Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCT
CTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"""

pprint.pprint(gcContent(example))


# WIP