def check_passcode(code):
    code = code.split()
    bag = set()
    for word in code:
        if word in bag:
            return False
        bag.add(word)

    return True

with open('input', 'r') as f:
    count = 0
    for line in f:
        valid = check_passcode(line)
        print valid
        if valid:
            count += 1
            
    print count
