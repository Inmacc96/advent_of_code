def readInput(filetxt):
    f = open(filetxt,'r')
    lines = f.read().splitlines()
    list_num = [int(x) for x in lines[0].split(',')]
    list_boards= []
    for (i,x) in enumerate(lines):
        if x=='':
            list_boards.append([[int(item) for item in x.split(' ') if item!=''] for x in lines[i+1:i+6]])
    f.close()
    return list_num, list_boards

def winning_score(filetxt):
    (list_num,list_boards) = readInput(filetxt)
    for num in list_num:
        for board in list_boards:
            for row in board:
                if num in row:
                    index = row.index(num)
                    row[index]='-'
                    if row ==['-']*5 or [num_rows[index] for num_rows in board] == ['-']*5:
                        sum_unmarked_number=sum([x for sub_list in board for x in sub_list if x!='-'])
                        return num*sum_unmarked_number

print('Solution 1: {}'.format(winning_score('input.txt')))


def last_winning_board_score(filetxt):
    (list_num,list_boards) = readInput(filetxt)
    len_total_boards=len(list_boards)
    winning_list_boards = []
    winning_nums = []
    for num in list_num:
        if len(winning_list_boards)!= len_total_boards:
            for board in list_boards:
                if board not in winning_list_boards:
                    for row in board:
                        if num in row:
                            index = row.index(num)
                            row[index]='-'
                            if row == ['-']*5 or [num_rows[index] for num_rows in board] == ['-']*5:
                                winning_nums.append(num)
                                winning_list_boards.append(board)
    sum_unmarked_number=sum([x for sub_list in winning_list_boards[-1] for x in sub_list if x!='-'])
    return winning_nums[-1]*sum_unmarked_number

print('Solution 2: {}'.format(last_winning_board_score('input.txt')))





