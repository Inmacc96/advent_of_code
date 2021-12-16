
def readInput(filetxt):
    f = open(filetxt,'r')
    data = f.read().splitlines()
    f.close()
    return data

def position_depth1(filetext):
    planned_course = readInput(filetext)
    forward=0
    depth=0
    for x in planned_course:
        if x[0] == 'f':
            forward+=int(x[-1])
        elif x[0] == 'd':
            depth+=int(x[-1])
        else:
            depth-=int(x[-1])
    return (forward,depth,forward*depth)

def position_depth2(filetext):
    planned_course = readInput(filetext)
    dicc = {}
    for x in planned_course:
        if x[0] in dicc.keys():
            dicc[x[0]] += int(x[-1])
        else:
            dicc[x[0]] = int(x[-1])
    forward=dicc['f']
    depth=dicc['d'] - dicc['u']
    return (forward,depth,forward*depth)

print('Solution 1:' + position_depth1('input.txt'))
print('Solution 1:' + position_depth2('input.txt'))

def position_depth_aim(filetext):
    planned_course = readInput(filetext)
    forward=0
    depth=0
    aim=0
    for x in planned_course:
        if x[0] == 'f':
            forward+=int(x[-1])
            depth += int(x[-1]) * aim
        elif x[0] == 'd':
            aim+=int(x[-1])
        else:
            aim-=int(x[-1])
    return (forward,depth,forward*depth)

print('Solution 2:' + position_depth_aim('input.txt'))
