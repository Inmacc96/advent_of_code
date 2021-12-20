import copy


def readInput(filetxt):
    f = open(filetxt,'r')
    data = [int(x) for x in f.read().splitlines()[0].split(',')]
    f.close()
    return data

def n_fuel_to_align(filetxt):
    crabs_pos = readInput(filetxt)
    fuel_cost = copy.copy(crabs_pos)
    fuel_cost_total = float('Inf')
    for i in range(max(crabs_pos)+1):
        for (j,pos) in enumerate(crabs_pos):
            fuel_cost[j] = abs(pos-i)
        if fuel_cost_total > sum(fuel_cost):
            fuel_cost_total = sum(fuel_cost)

    return fuel_cost_total
        
print('Solution 1: {}'.format(n_fuel_to_align('input.txt')))

def n_fuel_to_align2(filetxt):
    crabs_pos = readInput(filetxt)
    fuel_cost = copy.copy(crabs_pos)
    fuel_cost_total = float('Inf')
    for i in range(max(crabs_pos)+1):
        for (j,pos) in enumerate(crabs_pos):
            fuel_cost[j] = sum([x for x in range(abs(pos-i)+1)])
        if fuel_cost_total > sum(fuel_cost):
            fuel_cost_total = sum(fuel_cost)

    return fuel_cost_total
        
print('Solution 2: {}'.format(n_fuel_to_align2('input.txt')))

#Another way:
def n_fuel_to_align2_2(filetxt):
    crabs_pos = readInput(filetxt)
    fuel_cost = copy.copy(crabs_pos)
    fuel_cost_total = float('Inf')
    for i in range(max(crabs_pos)+1):
        for (j,pos) in enumerate(crabs_pos):
            fuel_cost[j] = (abs(pos-i)*(abs(pos-i)+1))/2
        if fuel_cost_total > sum(fuel_cost):
            fuel_cost_total = sum(fuel_cost)

    return fuel_cost_total
        
print('Solution 2: {}'.format(n_fuel_to_align2_2('input.txt')))