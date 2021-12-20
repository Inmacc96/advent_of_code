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
