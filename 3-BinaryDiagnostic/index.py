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




