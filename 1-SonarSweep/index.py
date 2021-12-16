def readInput(filetxt):
    f = open(filetxt,'r')
    data = f.read().splitlines()
    data = [int(x) for x in data]
    f.close()
    return data


measurements = readInput('input.txt')

def n_increases(measurements):
    cont = 0
    for (i,x) in enumerate(measurements):
        if i!= len(measurements)-1 and measurements[i] < measurements[i+1]:
            cont += 1

    return cont

print('Solution 1: {}'.format(n_increases(measurements)))

def n_sum_incresases(measurements):
    cont=0
    for (i,x) in enumerate(measurements):
        if sum(measurements[i+1:i+4]) > sum(measurements[i:i+3]):
            cont+=1
    return cont

#Otra forma
def n_sum_incresases2(measurements):
    cont=0
    suma = sum(measurements[0:3])
    for (i,x) in enumerate(measurements):
        if sum(measurements[i:i+3]) > suma:
            cont+=1
        suma = sum(measurements[i:i+3])
    return cont

print('Solution 2: {}'.format(n_sum_incresases(measurements)))
print('Solution 2.2: {}'.format(n_sum_incresases2(measurements)))




 
