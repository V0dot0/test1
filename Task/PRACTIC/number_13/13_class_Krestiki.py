
import math
import random

bord = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

bord_keys = []
for key in bord:
    bord_keys.append(key)

def printBord(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(999):

        if count == 9:
            print("\nКонец\n")
            print("Ничья")

        printBord(bord)

        print("Ваш шаг," + turn + ".Выберите место\n"
                                  "7-8-9\n"
                                  "4-5-6\n"
                                  "1-2-3\n ")

        while True:
            try:
                move = int(input('Выберите цифру, пожалуйста'))
                break
            except:
                print(" Это не цифра. ")

        while (int(move) > 9) or (int(move) < 1):
            print("Выберите цифру от 1 до 9")
            move = input()

        move = str(move)

        if bord[move] == ' ':
            bord[move] = turn
            count += 1
        else:
            print("Занято.\n Выберите другое место")
            continue

        if bord['7'] == bord['8'] == bord['9'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['4'] == bord['5'] == bord['6'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['1'] == bord['2'] == bord['3'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['1'] == bord['4'] == bord['7'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['2'] == bord['5'] == bord['8'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['3'] == bord['6'] == bord['9'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['7'] == bord['5'] == bord['3'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['1'] == bord['5'] == bord['9'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

# копия с примитывным ии
def gameAI():
    turn = 'X'
    count = 0

    for i in range(999):

        if count == 9:
            print("\nКонец\n")
            print("Ничья")

        printBord(bord)
        print("Ваш шаг," + turn + ".Выберите место\n"
                                  "7-8-9\n"
                                  "4-5-6\n"
                                  "1-2-3\n ")



        if turn == 'X':

            while True:
                try:
                    move = int(input('Выберите цифру, пожалуйста'))
                    break
                except:
                    print(" Это не цифра. ")

            while (int(move) > 9) or (int(move) < 1):
                print("Выберите цифру от 1 до 9")
                move = input()

            move = str(move)
        else:
            move = str(random.randint(1, 9))
        print("\n")

        if bord[move] == ' ':
            bord[move] = turn
            count += 1

        else:
            print("Занято.\n Выберите другое место")
            continue

        if bord['7'] == bord['8'] == bord['9'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['4'] == bord['5'] == bord['6'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['1'] == bord['2'] == bord['3'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['1'] == bord['4'] == bord['7'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['2'] == bord['5'] == bord['8'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['3'] == bord['6'] == bord['9'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['7'] == bord['5'] == bord['3'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break
        elif bord['1'] == bord['5'] == bord['9'] != ' ':
            printBord(bord)
            print("\nКонец\n")
            print(" **** " + turn + " победил. ****")
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'



useAi = input("Используем случайный ии? 1 = да, 2 = нет.")
if (useAi == "1" or useAi == "да"):
    gameAI()
else:
    game()

