with open('input', 'r') as f:
    jumps = []
    for jump in f:
        jumps.append(int(jump.strip()))

end = len(jumps)
pos = 0
c = 0

while (0 <= pos < end):
    offset = jumps[pos]
    jumps[pos] += (1 if offset < 3 else -1)
    pos += offset
    c += 1

print c
