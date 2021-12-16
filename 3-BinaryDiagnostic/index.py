def readInput(filetxt):
    f = open(filetxt,'r')
    data = f.read().splitlines()
    f.close()
    return data

def power_consumption(filetxt):
    num_binary = readInput(filetxt)
    gamma_rate = ''
    epsilon_rate = ''
    count_0 = [0] * len(num_binary[0])
    count_1 = [0] * len(num_binary[0])
    for num in num_binary:
        for (i,bit) in enumerate(list(num)):
            if bit == '0':
                count_0[i] +=1
            else:
                count_1[i] +=1
    for (i,j) in zip(count_0,count_1):
        if i>j:
            gamma_rate += '0'
            epsilon_rate += '1'
        else:
            gamma_rate += '1'
            epsilon_rate += '0'
    
    return (int(gamma_rate,2)*int(epsilon_rate,2))


print('Solution 1: {}'.format(power_consumption('input.txt')))

def life_support_rating(filetxt):
    num_binary = readInput(filetxt)
    oxygen_generator_rating = num_binary
    CO2_scrubber_rating = num_binary
    i=0
    j=0
    while len(oxygen_generator_rating) != 1:
        cont_0 = 0
        cont_1 = 0
        for num in oxygen_generator_rating:
            if list(num)[i] == '0':
                cont_0 +=1
            else:
                cont_1 +=1
        if cont_0 > cont_1:
            oxygen_generator_rating = [num for num in oxygen_generator_rating if list(num)[i]=='0']
        else:
            oxygen_generator_rating = [num for num in oxygen_generator_rating if list(num)[i]=='1']
        i+=1
    
    while len(CO2_scrubber_rating) != 1:
        cont_0 = 0
        cont_1 = 0
        for num in CO2_scrubber_rating:
            if list(num)[j] == '0':
                cont_0 +=1
            else:
                cont_1 +=1
        if cont_0 > cont_1:
            CO2_scrubber_rating = [num for num in CO2_scrubber_rating if list(num)[j]=='1']
        else:
            CO2_scrubber_rating = [num for num in CO2_scrubber_rating if list(num)[j]=='0']
        j+=1
    
    return (int(oxygen_generator_rating[0],2)*int(CO2_scrubber_rating[0],2))

print('Solution 2: {}'.format(life_support_rating('input.txt')))
        




