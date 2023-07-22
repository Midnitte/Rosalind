# Working With Files

def evenLines(s:str) -> str:
    """"Given: A file containing at most 1000 lines.
    Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines."""
    lines = [line for line in s.split("\n") if line]

    for count, line in enumerate(lines):
        if ((count+1)%2) == 0:
            print(line)
        else:
            pass
    

example = """Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat"""

#evenLines(example)

f = open("rosalind_ini5.txt", "r")

evenLines(f.read())