def readInput(filetxt):
    f = open(filetxt,'r')
    data = [x.split('|') for x in f.read().splitlines()]
    f.close()
    return data

def n_digits_1478(filetxt):
    signal_patterns_digits_ouput = readInput(filetxt)
    digits_output = [y.split(' ')[1:] for y in [x[1] for x in signal_patterns_digits_ouput]]
    count = 0
    for digits in digits_output:
        for digit in digits:
            if len(digit) in [2,4,3,7]:
                count +=1

    return count


print('Solution 1: {}'.format(n_digits_1478('input.txt')))