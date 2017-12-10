def check_passcode(code):
    code = code.split()
    bag = set()
    for word in code:
        word_val = sort_word(word)
        if word_val in bag:
            return False
        bag.add(word_val)

    return True

def sort_word(word):
    return ''.join(sorted(word))


with open('input', 'r') as f:
    count = 0
    for line in f:
        valid = check_passcode(line)
        print valid
        if valid:
            count += 1
    print count
