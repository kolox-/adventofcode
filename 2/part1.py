
filename = 'input'
with open (filename, 'r') as f:
    total = 0
    for line in f:
        line = line.split()
        print(line)
        max_ = int(line[0])
        min_ = int(line[0])
        for n in line:
            n = int(n)
            if n > max_:
                max_ = n
            if n < min_:
                min_ = n
        local_t = max_ - min_
        print(local_t)
        total += local_t
        #total += local_t
    print('done: {0}'.format(total))
