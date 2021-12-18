def readInput(filetxt):
    f = open(filetxt,'r')
    data=[]
    lines = f.read().splitlines()
    for line in lines:
        data.append([int(j) for i in [y.split(',') for y in [x for x in line.split() if x!='->']] for j in i])
    f.close()
    return data

def lines_map_create(lines):
    n_max = max([j for i in lines for j in i])
    lines_map = [[0] * (n_max+1) for i in range(n_max+1)]
    for line in lines:
        if line[1] == line[3]:
            if line[0] < line[2]:
                iter  = range(line[0],line[2]+1)
            else:
                iter = range(line[0],line[2]-1,-1)
            for i in iter:
                if lines_map[line[1]][i] != 0:
                    lines_map[line[1]][i]+= 1
                else:
                    lines_map[line[1]][i]=1
           
        if line[0] == line[2]:
            if line[1] < line[3]:
                iter  = range(line[1],line[3]+1)
            else:
                iter = range(line[1],line[3]-1,-1)
            for i in iter:
                if lines_map[i][line[0]] != 0:
                    lines_map[i][line[0]] += 1
                else:
                    lines_map[i][line[0]] =1

    return lines_map


def n_overlap_points(filetxt):
    lines = readInput(filetxt)
    lines_map = lines_map_create(lines)
    n_total_greater_2 = 0
    for row in lines_map:
        n_total_greater_2 += len([x for x in row if x>=2])
    return n_total_greater_2


print('Solution 1: {}'.format(n_overlap_points('input.txt')))




