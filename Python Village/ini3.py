# Strings and Lists

def humpty(s):
    """Given: A string s of length at most 200 letters and four integers a, b, c and d.
    Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice."""
    text, slices, _ = s.split("\n")
    slices = list(slices.split())
    a, b, c, d = [int(i) for i in slices]
    return f'{text[a:b+1]} {text[c:d+1]}'


example = """HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102"""

#print(humpty(example))

f = open("rosalind_ini3.txt", "r")

print(humpty(f.read()))
