# Calculate protein mass

def weightedAlph(p: str) -> float:
    """Given: A protein string P of length at most 1000 aa. 
    Return: The total weight of P."""
    def prots(codon: list) -> list:
        match codon:
            case "A":
                return 71.03711
            case "C":
                return 103.00919
            case "D":
                return 115.02694
            case "E":
                return 129.04259
            case "F":
                return 147.06841
            case "G":
                return 57.02146
            case "H":
                return 137.05891
            case "I" | "L":
                return 113.08406
            case "K":
                return 128.09496
            case "M":
                return 131.04049
            case "N":
                return 114.04293
            case "P":
                return 97.05276
            case "Q":
                return 128.05858
            case "R":
                return 156.10111
            case "S":
                return 87.03203
            case "T":
                return 101.04768
            case "V":
                return 99.06841
            case "W":
                return 186.07931
            case "Y":
                return 163.06333

    def translation(mrna):
        result = [prots(i) for i in mrna]
        return sum([int(elem) for elem in result])
    
    return translation(prots(p))

example = "SKADYEK"
print(weightedAlph(example))