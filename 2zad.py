# игровое поле со всеми ходами пользователей
board = list(range(1, 10))

wins_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]   # выигрышные комбинации

def draw_board():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|',
              board[2 + i * 3], '|')  # вывод игрового поля по строкам
    print('-------------')

def take_input(player_token):         # в параметр передаем символ пользователя
    while True:
        value = input('Куда поставим ' + player_token + '? ')
        # value обозначает название ключа, значение которого нужно вернуть
        if not (value in '123456789'):
            print('Вы ввели что-то не то... Try again')
            # попытка повторного ввода; возвращаем выполнение цикла в начало
            continue
        # если все нормально, то преобразуем value к целому типу
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Эта клетка уже занята')
            continue
        # если все нормально, то запишем в ячейку указанный знак (Х или О)
        board[value - 1] = player_token
        break                 # выходим из цикла

def check_win():
    for each in wins_coord:   # переменная each принимает каждый из кортежей списка
        # 0, 1, 2 - обращаемся к каждому числу в списках кортежа по его индексу
        if (board[each[0]-1]) == (board[each[1]-1]) == (board[each[2]-1]):
            return board[each[1]-1]
    else:                     # должно стоять не для условия, а для цикла, чтобы цикл прервался
        return False

def main():                   # объединим все
    counter = 0               # нумерация хода
    while True:
        draw_board()
        if counter % 2 == 0:  # каждый четный ход...
            take_input('X')   # ...будут ходить крестики
        else:
            take_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                draw_board()
                print(winner, 'Выиграл!')
                break
        counter += 1          # если кол-во ходов ещё не 3
        if counter > 8:       # чтобы программа не работала после заполнения поля
            draw_board()
            print('Ничья!')
            break

main()