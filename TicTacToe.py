def hello():
    welcome_text = "Добро пожаловать в Крестики - Нолики\n"
    rules = "" \
            "Для того, чтобы сделать ход,\n" \
            "введите номер строки, а затем  номер стобца через пробел.\n" \
            "      --------------\n" \
            "      Например: 1 0\n" \
            "      --------------\n" \

    luck = "Удачи ! \n"
    print(welcome_text, rules, luck, sep="- - - - - - - - - - - - - - - - - - -\n") #Вывод приветствия, правил и
                                                                                    # пож. удачи

field = [[" ", " ", " "] for i in range(3)]

def show_field():
    print(f"    0 | 1 | 2 |")
    print("---------------")
    for i in range(3):
        print(f"{i} | {field[i][0]} | {field[i][1]} | {field[i][2]} |")
        print("---------------")


def ask_coord():
    while True:
        line, col = map(int, input("Ваш ход: ").split())
        if line > 2 or line < 0 or col > 2 or col < 0:
            print("Координаты вне диапазона. Введите числа от 0 до 2!")
        else:
            if field[line][col] != " ":
                print("Клетка занята!")
            else:
                return line, col

def check_victory():
    x = ["X", "X", "X"]
    o = ["O", "O", "O"]

    victory_combin = [
        [field[0][0], field[0][1], field[0][2]],
        [field[1][0], field[1][1], field[1][2]],
        [field[2][0], field[2][1], field[2][2]],
        [field[0][0], field[1][0], field[2][0]],
        [field[0][1], field[1][1], field[2][1]],
        [field[0][2], field[1][2], field[2][2]],
        [field[0][0], field[1][1], field[2][2]],
        [field[2][0], field[1][1], field[0][2]],
    ]

    for i in range(8):
        if victory_combin[i] == x:
            print("КРЕСТКИ ПОБЕДИЛИ!")
            return False
        if victory_combin[i] == o:
            print("НОЛИКИ ПОБЕДИЛИ!")
            return False


def game():
    hello()
    show_field()
    turn = 0
    while True:
        turn += 1

        if turn % 2 == 0:
            print("Ходят Нолики!")
            line, col = ask_coord()
            field[line][col] = "O"
        else:
            print("Ходят Крестики!")
            line, col = ask_coord()
            field[line][col] = "X"

        show_field()

        if turn >= 3:
            if check_victory() is False:
                break

        if turn == 9:
            print("У ВАС НИЧЬЯ!")
            break

game()
