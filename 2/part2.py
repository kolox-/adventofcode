
def do_work(line):
    #line is already split
    line = line.split()
    for i, n in enumerate(line):
        n = int(n)
        for j in range(i+1, len(line)):
            m = int(line[j])
            if n % m == 0 or m % n == 0:
                return ((n/m) if n > m else (m/n))
    

filename = 'input'
with open (filename, 'r') as f:
    total = 0
    for line in f:
        print(line)
        result = do_work(line)
        print result
        total += result
    print('done: {0}'.format(total))
