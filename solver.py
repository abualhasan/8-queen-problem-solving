##########################################################################
r_pos = (int)(raw_input("enter the first queen row position : "))
c_pos = (int)(raw_input("enter the second queen col position : "))
print "\n"
initial_board = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
initial_board[r_pos][c_pos] = 1
##########################################################################
Num_Of_Queens = 0

def Check(List_Solu_Progress):
    global Num_Of_Queens
    if Num_Of_Queens == 8:
        return True
    else:
        for i in range(0, 8, 1):
            for j in range(0, 8, 1):
                if List_Solu_Progress[i][j] == 0:
                    Put_Queen_at_valid_place(List_Solu_Progress, i, j)
                    if Check(List_Solu_Progress):
                        return True
                    else:
                        Remove_Queen_From_Invalid_place(List_Solu_Progress, i, j)
        return False

def Put_Queen_at_valid_place(List_Solu_Progress, row_pos, col_pos):
    global Num_Of_Queens
    for i in range(0, 8, 1):
        List_Solu_Progress[i][col_pos] += 1  # put 1 s at the whole row
    for i in range(0, 8, 1):
        List_Solu_Progress[row_pos][i] += 1  # put 1 s at the whole col
    i = row_pos-1
    j = col_pos - 1
    while i >= 0 and j >= 0:
        List_Solu_Progress[i][j] += 1
        i -= 1
        j -= 1
    i = row_pos + 1
    j = col_pos + 1
    while i < 8 and j < 8:
        List_Solu_Progress[i][j] += 1
        i += 1
        j += 1
    i = row_pos + 1
    j = col_pos - 1
    while i < 8 and j >= 0:
        List_Solu_Progress[i][j] += 1
        i += 1
        j -= 1
    i = row_pos - 1
    j = col_pos + 1
    while i >= 0 and j < 8:
        List_Solu_Progress[i][j] += 1
        i -= 1
        j += 1
    List_Solu_Progress[row_pos][col_pos] += 100
    Num_Of_Queens += 1

def Remove_Queen_From_Invalid_place(List_Solu_Progress, row_pos, col_pos):
    global Num_Of_Queens
    for i in range(0, 8, 1):
        List_Solu_Progress[i][col_pos] -= 1
    for i in range(0, 8, 1):
        List_Solu_Progress[row_pos][i] -= 1
    i = row_pos - 1
    j = col_pos - 1
    while i >= 0 and j >= 0:
        List_Solu_Progress[i][j] -= 1
        i -= 1
        j -= 1
    i = row_pos + 1
    j = col_pos + 1
    while i < 8 and j < 8:
        List_Solu_Progress[i][j] -= 1
        i += 1
        j += 1
    i = row_pos + 1
    j = col_pos - 1
    while i < 8 and j >= 0:
        List_Solu_Progress[i][j] -= 1
        i += 1
        j -= 1
    i = row_pos - 1
    j = col_pos + 1
    while i >= 0 and j < 8:
        List_Solu_Progress[i][j] -= 1
        i -= 1
        j += 1
    List_Solu_Progress[row_pos][col_pos] -= 100
    Num_Of_Queens -= 1

def Creat_Solu_Board():
    start_temp = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]

    row_pos = r_pos
    col_pos = c_pos
    Put_Queen_at_valid_place(start_temp, row_pos, col_pos)

    print"  [",r_pos, "]", "[",c_pos, "] \n"
    print_user_choice(initial_board)
    print"  _____________________________\n "
    print"  the solution  is : "


    return start_temp

def Print_Solu_Board(List_Solu_Progress):
    temp = ""
    for j in range(0, 8, 1):
        temp += "    "
    temp += "\n"
    for i in range(0, 8, 1):
        for j in range(0, 8, 1):
            temp += "    "
        temp += " \n"
        for j in range(0, 8, 1):
            if List_Solu_Progress[i][j] > 10:
                temp += "  1 "
            else:
                temp += "  0 "
        temp += "  "
        for j in range(0, 8, 1):
            temp += "   "

    print (temp)

def print_user_choice(l):
    for m in l:
        print " ", m[0], " ", m[1], " ", m[2], " ", m[3], " ", m[4], " ", m[5], " ", m[6], " ", m[7], " ", "\n"

###########################################################################

board = Creat_Solu_Board()
Check(board)
Print_Solu_Board(board)