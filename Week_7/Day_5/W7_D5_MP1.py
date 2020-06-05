import random
import time
#Welcome message (presenting auto)
welcome = input("Welcome to the Tic-Tac-Toe game.")
rules = input("You need to enter a num of cell 1-9 (counting from left top cell)")


buttons = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
choice = []

for sign in buttons:
    choice.append(sign)

#Bord
def show_cells(cell):
    print(cell['1'] + '|' + cell['2'] + '|' + cell['3'])
    print('-+-+-')
    print(cell['4'] + '|' + cell['5'] + '|' + cell['6'])
    print('-+-+-')
    print(cell['7'] + '|' + cell['8'] + '|' + cell['9'])
    print('-+-+-')

#play

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        show_cells(buttons)
        print("Yor turn," + turn + " ""Enter a number of cell\n>>>")

        move = input()

        if buttons[move] == ' ':
            buttons[move] = turn
            count += 1
        else:
            print("Choice another cell. Enter a number of cell\n>>>")
            continue

#conditions
        if count >= 5:
            if buttons['1'] == buttons['2'] == buttons['3'] != ' ':
                show_cells(buttons)
                print("Game Over!\n Winner is" + turn)
                break

            elif buttons['4'] == buttons['5'] == buttons['6'] != ' ':
                show_cells(buttons)
                print("Game Over!\n Winner is" + turn)
                break
            elif buttons['7'] == buttons['8'] == buttons['9'] != ' ':
                show_cells(buttons)
                print("Game Over!\n Winner is" + turn)
                break
            elif buttons['1'] == buttons['4'] == buttons['7'] != ' ':
                show_cells(buttons)
                print("Game Over!\n Winner is" + turn)
                break
            elif buttons['2'] == buttons['5'] == buttons['8'] != ' ':
                show_cells(buttons)
                print("Game Over!\n Winner is" + turn)
                break
            elif buttons['3'] == buttons['6'] == buttons['9'] != ' ':
                show_cells(buttons)
                print("Game Over!\n Winner is" + turn)
                break
            elif buttons['3'] == buttons['5'] == buttons['7'] != ' ':
                show_cells(buttons)
                print("Game Over!\n Winner is" + turn)
                break
            elif buttons['1'] == buttons['5'] == buttons['9'] != ' ':
                show_cells(buttons)
                print("Game Over!\n Winner is" + turn)
                break

        if count == 9:
            print("Game Over!\n No winner")
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    again = input("Again?(y/n)\n>>>")
    if again == 'y':
        for sign in buttons:
            buttons[sign] = ' '
        game()
if __name__ == "__main__":
    game()

#To Choice X or O
# def inputPlayerLetter():
#     letter = ''
#     while not (letter == 'X' or letter == 'O'):
#         print('Do you want to be X or O?')
#         letter = input().upper()
#         if letter == 'X':
#             return ['X', 'O']
#         else:
#             return ['O', 'X']

#Display "Player 1" and "Player 2"
# name1 = input("Enter your name Player 1\n>>>")
# print("Hi, {}".format(name1))
# name2 = input("Enter your name Player 2\n>>>")
# print("Hi, {}".format(name2))
# time.sleep(2)