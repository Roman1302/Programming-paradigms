import os

clear = lambda: os.system('clear')
clear()

print('Игра "Крестики-Нолики"')

field = list(range(1, 10))


def creating_field(field):
    print("=" * 13)
    for i in range(3):
        print("|", field[0 + i * 3], "|", field[1 + i * 3], "|", field[2 + i * 3], "|")
        print("=" * 13)


def cell_selection(player_move):
    valid = False
    while not valid:
        player_answer = input("Введи номер ячейки для " + player_move + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод! Нужно вводить число!")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer - 1]) not in "XO"):
                field[player_answer - 1] = player_move
                valid = True
            else:
                print("Ячейка уже занята")
        else:
            print("Некорректный ввод. Введи число от 1 до 9.")


def check_win(field):
    winning_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in winning_combination:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def game(field):
    counter = 0
    win = False
    while not win:
        creating_field(field)
        if counter % 2 == 0:
            cell_selection("X")
        else:
            cell_selection("O")
        counter += 1
        # creating_field(field)
        if counter > 4:
            tmp = check_win(field)
            if tmp:
                print("\nУРАААА!", tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("\nНичья!")
            break
    creating_field(field)


game(field)
