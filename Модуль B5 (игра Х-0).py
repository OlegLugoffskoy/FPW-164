import random

game_field = [['1 ', '2 ', '3 '], ['4 ', '5 ', '6 '], ['7 ', '8 ', '9 ']]  # список визуализирующий поле игры
spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # из этого списка буду удалять выпавшие элемены (которые выбрали)


def get_result():
    """ Функция проверяет выигрышные комбинации и если они есть возвращает 1 """
    for i in game_field:
        if i == [chr(10060), chr(10060), chr(10060)]:  # проверяю строковые выигршные комбинации (крестики)
            print('Победа игрока за крестики', chr(10060))
            return 1
        if i == [chr(11093), chr(11093), chr(11093)]:  # проверяю строковые выигршные комбинации (нолики)
            print('Победа игрока за нолики', chr(11093))
            return 1
    lst = []  # создаю пустой лист, в который буду складывать, поочередно, все элементы из game_field
    for i in game_field:
        for j in i:
            lst.append(j) # складываю все элементы из game_field для того чтобы к ним можно было обратиться по индексу
    if any([(lst[0] == chr(10060) and lst[3] == chr(10060) and lst[6]) == chr(10060),  # выигршные комбинации (крестики)
            (lst[1] == chr(10060) and lst[4] == chr(10060) and lst[7]) == chr(10060),  # по вертикалям
            (lst[2] == chr(10060) and lst[5] == chr(10060) and lst[8]) == chr(10060),
            (lst[0] == chr(10060) and lst[4] == chr(10060) and lst[8]) == chr(10060),  # и диагоналям
            (lst[2] == chr(10060) and lst[4] == chr(10060) and lst[6]) == chr(10060)]):
            print('Победа игрока за крестики', chr(10060))
            return 1
    elif any([(lst[0] == chr(11093) and lst[3] == chr(11093) and lst[6]) == chr(11093),  # аналогично для ноликов
            (lst[1] == chr(11093) and lst[4] == chr(11093) and lst[7]) == chr(11093),
            (lst[2] == chr(11093) and lst[5] == chr(11093) and lst[8]) == chr(11093),
            (lst[0] == chr(11093) and lst[4] == chr(11093) and lst[8]) == chr(11093),
            (lst[2] == chr(11093) and lst[4] == chr(11093) and lst[6]) == chr(11093)]):
            print('Победа игрока за нолики', chr(11093))
            return 1
    else:
        return 0

def output_screen(choice_player1, choice_player2):
    """Функция визуализирует игру, выводя на экран текущее положение на доске
    параметр choice_player1 - выбор игрока 1
    параметр choice_player2 - выбор игрока 2"""
    # global game_field  # переменную game_field помещаю в глабальную облать видиммости (если потребуется)
    for row in game_field:  # итерирую игровое поле по строкам
        for el in row: # каждую строку итерирую по элементам
            if el == str(choice_player1)+' ':  # привожу переданый параметр 1 к единому типу с элементами и сравниваю
                ind = row.index(el)  # когда искомый эл-т найден в списке, определяю его индекс в строке
                row[ind] = chr(10060)  # и меняю значение на крестик, обратившись за ним по номеру в юникоде
            if el == str(choice_player2)+' ':  # аналогичные действия, для ноликов
                ind = row.index(el)
                row[ind] = chr(11093)
    for i in game_field:
        print(i)


def man_vs_man():
    """ Функция алгоритма игры человека с человеком """
    while True:
        if spisok is []:  # если список пуст, игра заканчивается в ничью
            print("Ничья")
            print("Игра закончена")
            break
        elif get_result():  # если функция возвращает True, выполнилось одно из условий и игра заканчивается победой
            print("Игра закончена")
            break
        else:  # если функция возвращает False и spisok не пуст игра продолжается
            try:
                choice_player1 = int(input(f"Выбирите позицию для {chr(10060)} от 1 до 9: "))  # выбор игрока 1
                spisok.remove(choice_player1)  # из списка удаляется выбранный элемент
                choice_player2 = 0  # выбор игрока 2 ещё не сделан
                get_result()  # запускаю функцию проверяющаю выигрышные комбинации
                output_screen(choice_player1, choice_player2)  # вывожу на экран игровое поле на текущий момент
                # Для второго игрока аналогичный алгоритм:
                choice_player2 = int(input(f"Выбирите позицию для {chr(11093)} от 1 до 9: "))
                spisok.remove(choice_player2)
                get_result()
            except ValueError:
                print('Игрок выбрал выпавшую позицию и пропустил ход. Будьте внимательнее!')
            output_screen(choice_player1, choice_player2)
            print("-------------------")

# Функция аналогичная предыдущей, только выбор компа осуществляется с помощью метода choice() из модуля random
def man_vs_comp():
    """ Функция алгоритма игры человека с компьютером """
    while True:
        if spisok == []:
            print("Ничья")
            break
        elif get_result():
            print("Игра закончена")
            break
        else:
            choice_player2 = random.choice(spisok)
            spisok.remove(choice_player2)
            choice_player1 = 0
            get_result()
            output_screen(choice_player1, choice_player2)

            choice_player1 = int(input("Сделайте выбор от 1 до 9: "))
            spisok.remove(choice_player1)
            get_result()
            output_screen(choice_player1, choice_player2)
            print("-------------------")


def game_cover():
    print("Добро пожаловать в игру крестики-нолики. Правила игры просты и приведены ниже.")
    for i in game_field:
        print(i)
    print("""Перед вами игровое поле, с позициями от 1 до 9. В выбранную вами позицию попадает крестик/нолик.
                                        Варианты игры:
    1. Человек vs человек. Тот игрок который побеждает в жеребьевке ходит первым крестиками. 
    2. Человек vs компьютер. Компьютер всегда ходит первым, ввиду неразвитого интеллекта\n""")
    print('Для продолжения игры сделайте выбор с кем вы хотите играть. 1 - с человеком, 2 - с компьютером')
    choice = input("Введите цифру 1 или 2 для выбора или любую другую цифру для выхода: ")
    if int(choice) == 1:  # если выбор игрока '1', то игра против человека:
        print("\nВы выбрали вариант игры: человек vs человек. Для продолжения вам нужно пройти жеребьевку:")
        choice = input("Сделайте выбор: Нажмите: '1' - это ОРЁЛ, любая другая цифра - это РЕШКА ")
        random_choice = random.randint(1, 2)  # случайный выбор орел/решка сохраняю в переменную
        if int(choice) == random_choice:  # если выбор игрока совпал с рандомным выбором, он ходит первым, крестиками
            print("Победил игрок выбравший орла, он ходит первым, крестиками", chr(10060))
            man_vs_man()  # запускается функция с алгоритмом игры человек против человека
        else:  # иначе, игрок ходит вторым, ноликами
            print("Победил игрок выбравший решку, он ходит первым, крестиками", chr(10060))
            man_vs_man()  # запускается функция с алгоритмом игры человек против человека
    elif int(choice) == 2:  # если выбор игрока '2', то игра против компьютера:
        print("\nВы выбрали вариант игры: человек vs компьютер. Компьютер ходит первым, ноликами", chr(11093))
        man_vs_comp()  # запускается функция с алгоритмом игры человек против компьютера
    else:  # если выбрана какая то другая цифра игра завершается
        print("Вы вышли из игры")


game_cover()  # запуск игры































# for i in game_field:
#     for j in i:
#         if j == choice_player:
#             ind = i.index(j)
#             i[ind] = 'x'
#             spisok.remove(choice_player)
#             choice_comp = random.choice(spisok)
#             spisok.remove(int(choice_comp))
#             ind_comp = i.index(int(choice_comp))
#             i[ind_comp] = '0'




# import random
#
# lst = []
# for row in range(3):
#     for column in range(3):
#         lst.append(tuple([str(row), str(column)]))
#
# print(lst)
#
#
# # choice_player = input("Введите через пробел строку/столбец:"))
#
#
# choice_player = '1 1'
# choice_player = tuple(choice_player.split())
# print(choice_player)
# lst.remove(choice_player)
# print(lst)
# choice_comp = random.choice(lst)
# print(choice_comp)

# str1 = '_|_|_'
# str1 = '_|_|_'
# str3 = ' | |'
#

#
# if choice_player[0] == '0':
#     if choice_player[1] == '0':
#         str1 = "x| | "
#     elif choice_player[1] == '1':
#         str1 = " |x| "
#     else:
#         str1 = "_|_|x"
# elif choice_player[0] == '1':
#     if choice_player[1] == '0':
#         str2 = "x|_ | "
#     elif choice_player[1] == '1':
#         str2 = "_|x|_"
#     else:
#         str2 = " | |x"
# else:
#     if choice_player[1] == '0':
#         str3 = "x| | "
#     elif choice_player[1] == '1':
#         str3 = " |x| "
#     else:
#         str3 = " | |x"
# print(f"{str1}\n{str2} \n{str3}")
