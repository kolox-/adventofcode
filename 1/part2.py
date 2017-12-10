with open ('input', 'r') as f:
    string = f.readline()
    c = 0
    length = len(string)
    offset = length/2
    for i, x in enumerate(string):
        pair_i = (i + offset) % length
        if string[i] == string[pair_i]:
            c += int(x)
    print c
