def readInput(filetxt):
    f = open(filetxt,'r')
    data = [int(x) for x in f.read().splitlines()[0].split(',')]
    f.close()
    return data

def n_lanternfish_after_80_days(filetxt):
    initial_state = readInput(filetxt)
    state = initial_state
    for i in range(0,80):
        for (i,x) in enumerate(state):
            if x>0:
                state[i] = x-1
            else:
                state[i] = 6
                state.append(9)

    
    return len(state)

print('Solution 1: {}'.format(n_lanternfish_after_80_days('input.txt')))