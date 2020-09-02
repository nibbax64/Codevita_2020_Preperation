from time import sleep
from platform import system
import os
def val(ch):
    VAL = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11}
    return VAL[ch]

def ogre(match, pos, command):
    if(command == 1):
        if(not checkFor(match, 'Z', pos)):
            match[pos[0]][pos[1]] = 'O'
    elif(command == 2):
        try:
            if(not checkFor(match, 'Z', pos)):
                match[pos[0]][pos[1]] = 'O'
            if(not checkFor(match, 'Z', [pos[0],pos[1]-1])):
                match[pos[0]][pos[1]-1] = 'O'
            if(not checkFor(match, 'Z', [pos[0]-1,pos[1]-1])):
                match[pos[0]-1][pos[1]-1] = 'O'
            if(not checkFor(match, 'Z', [pos[0]-1,pos[1]])):
                match[pos[0]-1][pos[1]] = 'O'
            if(not checkFor(match, 'Z', [pos[0]-1,pos[1]+1])):
                match[pos[0]-1][pos[1]+1] = 'O'
            if(not checkFor(match, 'Z', [pos[0],pos[1]+1])):
                match[pos[0]][pos[1]+1] = 'O'
            if(not checkFor(match, 'Z', [pos[0]+1,pos[1]+1])):
                match[pos[0]+1][pos[1]+1] = 'O'
            if(not checkFor(match, 'Z', [pos[0]+1,pos[1]])):
                match[pos[0]+1][pos[1]] = 'O'
            if(not checkFor(match, 'Z', [pos[0]+1,pos[1]-1])):
                match[pos[0]+1][pos[1]-1] = 'O'
        except:
            print("Ogre - OverFlow")
        finally:
            pass
    elif(command == 3):
        try:
            if(not checkFor(match, 'Z', pos)):
                match[pos[0]][pos[1]] = 'O'
            if(not checkFor(match, 'Z', [pos[0],pos[1]-1])):
                match[pos[0]][pos[1]-1] = '-'
            if(not checkFor(match, 'Z', [pos[0]-1,pos[1]-1])):
                match[pos[0]-1][pos[1]-1] = '-'
            if(not checkFor(match, 'Z', [pos[0]-1,pos[1]])):
                match[pos[0]-1][pos[1]] = '-'
            if(not checkFor(match, 'Z', [pos[0]-1,pos[1]+1])):
                match[pos[0]-1][pos[1]+1] = '-'
            if(not checkFor(match, 'Z', [pos[0],pos[1]+1])):
                match[pos[0]][pos[1]+1] = '-'
            if(not checkFor(match, 'Z', [pos[0]+1,pos[1]+1])):
                match[pos[0]+1][pos[1]+1] = '-'
            if(not checkFor(match, 'Z', [pos[0]+1,pos[1]])):
                match[pos[0]+1][pos[1]] = '-'
            if(not checkFor(match, 'Z', [pos[0]+1,pos[1]-1])):
                match[pos[0]+1][pos[1]-1] = '-'
        except:
            print("Ogre - OverFlow")
        finally:
            pass
    else:
        if(not checkFor(match, 'Z', pos)):
            match[pos[0]][pos[1]] = '-'
    return match

zs = [1,1]
def zeeSNAKE(match, pos, command):
    global zs
    if(command == 1):
        if(pos[0] == 0 or pos[0] == 11):
            zs[0] *= -1
        temp = [pos[0]+zs[0], pos[1]]
        match[pos[0]+zs[0]][pos[1]] = 'Z'
    if(command == 0):
        if(pos[1] == 0 or pos[1] == 11):
            zs[1] *= -1
        temp = [pos[0], pos[1]+zs[1]]
        match[pos[0]][pos[1]+zs[1]] = 'Z'
    # print(temp)
    return [temp, match]

def checkFor(match, devil, pos):
    if(match[pos[0]][pos[1]] == devil):
        return True
    else:
        return False

xixi = []
xixi_f = False
def fill_xixi(flag):
    if(flag == True):
        for i in range(12):
            for j in range(12):
                if((i+j)%2 == 0):
                    xixi.append([i,j])
    else:
        for i in range(12):
            for j in range(12):
                if((i+j)%2 != 0):
                    xixi.append([i,j])
    return

def show_board(match):
    for rows in match:
        for elem in rows:
            print(f'[{elem}]\t',end="")
        print()

def check_status(match, angel_pos):
    if(match[angel_pos[0]][angel_pos[1]] in ['Z','O']):
        return False
    elif(angel_pos in xixi and xixi_f == True):
        return False
    else:
        return True

def game(angel_pos_0, devil_types, devil_pos_0):
    global xixi_f
    angel_pos_0 = list(angel_pos_0)

    angel_pos_0[0],angel_pos_0[1] = int(angel_pos_0[1])-1,val(angel_pos_0[0])
    if(angel_pos_0 == [0,0] or angel_pos_0 == [0,11] or angel_pos_0 == [11,0] or angel_pos_0 == [11,11]):
        return False
    if(angel_pos_0[0] in range(1,11) and angel_pos_0[1] in range(1,11)):
        return False
    angel_pos_00 = angel_pos_0.copy()

    if(angel_pos_0[0] == 0):
        angel_shift = (1,0)
    elif(angel_pos_0[0] == 11):
        angel_shift = (-1,0)
    elif(angel_pos_0[1] == 0):
        angel_shift = (0,1)
    else:
        angel_shift = (0,-1)

    board = [['-' for i in range(12)] for _ in range(12)]
    devil_positions = {'O':[], 'X':[], 'Z':[]}

    for i in range(len(devil_types)):
        board[int(devil_pos_0[i][1:])-1][val(devil_pos_0[i][0])] = devil_types[i]
        devil_positions[devil_types[i]].extend([int(devil_pos_0[i][1:])-1,val(devil_pos_0[i][0])])
    board[angel_pos_0[0]][angel_pos_0[1]] = 'A'

    if(system() == 'Windows'):
        clear = 'cls'
    else:
        clear = "clear"

    os.system(clear)
    show_board(board)
    input("[ENTER]")

    count = 1
    if((devil_positions['X'][0]+devil_positions['X'][1])%2 == 0):
        fill_xixi(True)
    else:
        fill_xixi(False)

    while(True):

        os.system(clear)
        print(f'SEC - {count}')

        #changes to board
        board = ogre(board, devil_positions['O'], count%4)
        temp = zeeSNAKE(board, devil_positions['Z'], count%2)
        devil_positions['Z'] = temp[0]
        board = temp[1]
        if(count%8 == 0):
            xixi_f = True
            board[devil_positions['X'][0]][devil_positions['X'][1]] = 'X'
        else:
            xixi_f = False
            board[devil_positions['X'][0]][devil_positions['X'][1]] = '-'

        if(check_status(board, [angel_pos_0[0]+angel_shift[0],angel_pos_0[1]+angel_shift[1]])):
            board[angel_pos_0[0]][angel_pos_0[1]] = '-'
            board[angel_pos_0[0]+angel_shift[0]][angel_pos_0[1]+angel_shift[1]] = 'A'
            angel_pos_0[0],angel_pos_0[1] = angel_pos_0[0]+angel_shift[0],angel_pos_0[1]+angel_shift[1]
            if(((angel_pos_00[0]+angel_pos_0[0] == 11) or (angel_pos_00[1]+angel_pos_0[1] == 11))):
                board[angel_pos_0[0]][angel_pos_0[1]] = 'G'
                break
        else:
            board[angel_pos_0[0]][angel_pos_0[1]] = '-'
            board[angel_pos_0[0]+angel_shift[0]][angel_pos_0[1]+angel_shift[1]] = 'a'
            break

        show_board(board)
        sleep(0.5)

        count += 1

    show_board(board)
    return "DONE"

import random
if __name__ == "__main__":

    if(random.choice([True, False])):
        angel_pos_0 = tuple([random.choice(['B','C','D','E','F','G','H','I','J','K']),str(random.choice([1,12]))])
    else:
        angel_pos_0 = tuple([random.choice(['A','L']),str(random.randint(2,11))])
    devil_types = ('X','Z','O')
    devil_pos_0 = tuple([f"{random.choice(['A','B','C','D','E','F','G','H','I','J','K','L'])}{str(random.randint(1,12))}" for _ in range(3)])
    print(angel_pos_0)
    print(devil_types)
    print(devil_pos_0)
    input("ENTER")
    # raise SystemExit
    print(game(angel_pos_0, devil_types, devil_pos_0))
