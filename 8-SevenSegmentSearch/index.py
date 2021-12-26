def readInput(filetxt):
    f = open(filetxt,'r')
    data = [x.split('|') for x in f.read().splitlines()]
    f.close()
    return data

def n_digits_1478(filetxt):
    signal_patterns_digits_output = readInput(filetxt)
    digits_output = [y.split(' ')[1:] for y in [x[1] for x in signal_patterns_digits_output]]
    count = 0
    for digits in digits_output:
        for digit in digits:
            if len(digit) in [2,4,3,7]:
                count +=1

    return count


print('Solution 1: {}'.format(n_digits_1478('input.txt')))

def segments_config(signal_patterns):
    config=[0 for x in range(7)]
    digit_1 = [x for x in signal_patterns if len(x)==2][0]
    digit_7 = [x for x in signal_patterns if len(x)==3][0]
    not_common_letter_71 = list(set(digit_7)- set(digit_1))
    config[0] = not_common_letter_71[0]
    config[3] = list(digit_1)
    config[6] = list(digit_1)
    digit_4 = [x for x in signal_patterns if len(x)==4][0]
    not_common_letter_41 = list(set(digit_4)- set(digit_1))
    config[1] = not_common_letter_41
    config[2] = not_common_letter_41
    digits_235 = [x for x in signal_patterns if len(x)==5]
    common_letter_235 = list(set(digits_235[0]).intersection(digits_235[1],digits_235[2]))
    for letter in common_letter_235:
        if letter!=config[0]:
            if letter in config[2]:
                config[2] = letter
                config[1] = [x for x in config[1] if x != letter][0]
            else:
                config[5] = letter
    letter_in_config = []
    for x in config:
        if x!=0:
            if len(x) == 1:
                letter_in_config.append(x)
            else:
                letter_in_config.append(x[0])
                letter_in_config.append(x[1])
    config[4]= list(set(['a','b','c','d','e','f','g']) - set(letter_in_config))[0]
    det_pos_36 = [0 for x in range(7)]
    digits_25 = [x for x in digits_235 if not (config[3][0] in x and config[3][1] in x)]
    for letter in list(digits_25[0]):
        if letter not in config[3]:
            i = config.index(letter)
            det_pos_36[i]=1
    if det_pos_36[1] == 0 and det_pos_36[6] == 0:
        config[3] = [letter for letter in list(digits_25[0]) if letter in config[3]][0]
        config[6] = [x for x in config[6] if x!=config[3]][0]
    if det_pos_36[3] == 0 and det_pos_36[4] == 0 and det_pos_36[6] == 0:
        config[6] = [letter for letter in list(digits_25[0]) if letter in config[3]][0]
        config[3] = [x for x in config[3] if x!=config[6]][0]
    return config

def decoding_number(filetxt):
    Input = readInput(filetxt)
    decoded_numbers = []
    digits_pos = {'0': [0,1,3,4,6,5],
                  '1': [3,6],
                  '2': [0,3,2,4,5],
                  '3': [0,3,2,6,5],
                  '4': [1,2,3,6],
                  '5': [0,1,2,6,5],
                  '6': [0,1,2,6,5,4],
                  '7': [0,3,6],
                  '8': [0,1,2,3,4,5,6],
                  '9': [0,1,2,3,6,5]}
    for line in Input:
        signal_patterns = line[0].split(' ')[:-1]
        digits_output = line[1].split(' ')[1:]
        config = segments_config(signal_patterns)
        encoded_digit_pos = []
        for digit in digits_output:
            encoded_digit_pos_digit = []
            for letter in digit:
                encoded_digit_pos_digit.append(config.index(letter))
            encoded_digit_pos.append(encoded_digit_pos_digit)
        decoded_digit = ''
        for encoded_digit in encoded_digit_pos:
            for digit in digits_pos:
                if sorted(digits_pos[digit]) == sorted(encoded_digit):
                    decoded_digit += digit
        decoded_numbers.append(int(decoded_digit))

    return sum(decoded_numbers)


print('Solution 2: {}'.format(decoding_number('input.txt')))








