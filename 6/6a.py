import operator

def redistribute(banks):
    i, _ = max(enumerate(banks), key=operator.itemgetter(1))
    blocks = banks[i]
    banks[i] = 0
    while blocks != 0:
        i = (i + 1) % len(banks)
        banks[i] += 1
        blocks -= 1
    return banks
        
with open('input','r') as f:
    line = f.read()
    banks = line.split()
    banks = [int(x) for x in banks]

seen = set()
c = 0
while (True):
    configuration = tuple(banks)
    if configuration in seen:
        break
    seen.add(configuration)
    redistribute(banks)
    c += 1

print c
