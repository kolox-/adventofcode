


with open ('input', 'r') as f:
    string = f.readline()
    c = 0
    t = 0 
    for i, x in enumerate(string):
        t += 1
        try:
            if string[i] == string[i+1]:
                c += int(x)
        except:
            print("Reached the end!")

    if string[0] == string[-1]:
        c += int(string[0])
    print c
    print t
