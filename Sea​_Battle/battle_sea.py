import random
import time


print("Рекомендуемые параметры игровой доски =  7, 8, 9 клеток")
print("Если вы хотите поле меньших размеров нужно убавить количество короблей в конструкторе класса Ship")

size = input('Введите размер игровой доски:')
if isinstance(size, int):
    size_board = 8
else:
    size_board = int(size) + 1


class GameBoard:
    """
    Класс игровой доски:
    Конструктор принимает: параметр size, который задаёт размеры игрового поля (size x size).
    Второй параметр это список, индексы которого соответствуют индексам игрового поля.
    Метод change_board создаёт пустую игровую доску в соответствии с заданым размером.
    Метод get_cords создаёт словарь с ключами-координатыми игрового поля и их значениями ввиде индексов.
    visual_board формирует визуальное отображение доски на экране.
    """
    def __init__(self, size=size_board, board_lst=[0]) -> None:
        self.size = size
        self.board_lst = self.change_board()

    def change_board(self) -> list:
        """
        Метод заменяет элементы списка. Каждый 'size' элемент списка, на номер по порядку от 1 до размера доски.
        :return: возвращает список типа игровой доски, клетки поля пока заполнены нулями
        Вернувшийся список, для доски размером 3х3, имеет вид: [0, 1, 2, 3, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0]

        """
        board_lst = [0] * self.size ** 2  # заполняем нулями список длинной size x size
        count = 1
        for i in range(self.size, len(board_lst), self.size):  # меняю каждый size эл-т списка на номер по порядку
            if board_lst[i] == 0:
                board_lst[i] += count
                count += 1
        for i in range(0, self.size):  # меняю первые size элементов списка на номера по порядку (1, 2, 3, ..., size)
            board_lst[i] = i
        return board_lst  # возвращаем список из нулей соответствущий размеру клеток игрового поля

    def get_cords(self) -> dict:
        """
        Метод формирует словарь из координат и их индексов, которые соответствуют индексам игрового поля.
        Для доски 3х3 имеет вид: {'11': 5, '12': 6, '13': 7, '21': 9, '22': 10, '23': 11, '31': 13, '32': 14, '33': 15}
        :return: словарь {корды : индексы}.  """
        cnt = 0
        coord_dist = {}
        for i in range(self.size):
            for j in range(self.size):
                coord_dist[(str(i) + str(j))] = cnt
                cnt += 1
        coords_dist = {k: v for k, v in coord_dist.items() if int(k[0]) != 0 and int(k) % 10 != 0}
        return coords_dist

    def visual_board(self, list1: list, list2: list) -> None:
        """
        Визуализация игрового поля. Приводит списки игровых досок к следующему выиду:
        [0, 1. 2, 3]   [0, 1. 2, 3]
        [1, -. -, -]   [1, -. -, -]   Список со вложенными в него списками равными размеру поля,
        [2, -. -, -]   [2, -. -, -]   будут построчно выводиться на экран как показано слева
        [3, -. -, -]   [3, -. -, -]
        :param list1: список, который нужно преобразить и вывести на экран (доска компа)
        :param list2: список, который нужно преобразить и вывести на экран (доска пользователя)
        :return: None
        """
        print("============   Поле компьютера:  ===============      ==============  Поле пользователя:  ==============")
        playing_board1 = [list1[i:i + self.size] for i in range(0, len(list1), self.size)]
        playing_board2 = [list2[i:i + self.size] for i in range(0, len(list2), self.size)]
        for i in range(len(playing_board1)):
            print(str(playing_board1[i]), "   ", str(playing_board2[i]))
        print('========================================================================================================')


class Ship:
    def __init__(self, size=size_board, onedeck=4, twodeck=2, threedeck=1):
        self.size = size  # размер игрового поя size x size
        self.onedeck = onedeck      # количество однопалубных корблей
        self.twodeck = twodeck      # количество двухпалубных корблей
        self.threedeck = threedeck  # количество трёхпалубных корблей
        self.index_list = [i for i in GameBoard(self.size).get_cords().values()]  # индексы (клетки) поля боя
        self.ship_list = []  # сюда будут помещены списки с индексами кораблей, которые разместятся на доске

    def add_ship_threedeck(self) -> list:
        """
        Метод добавления 3-х палубного корабля на игровое поле.
        Рандомно выбирается ориентация корабля (вертикальная или горизонтальная).
        Выбирается случайный индекс, из списка индексов в котором может размещаться клетка (палуба) корабля.
        Этот индекс является стартовой точкой, от которой будут строиться палубы корабля.
        В зависимости от ориентации, определяется ещё 2 свободных индекса, которые примыкают к стартовой точке.
        Каждый из выбранных индексов помещается в ранее созданный список, таким образом мы получаем список из
        трёх точек-индексов корабля.

        :return: список с индексами соответствующими "полю боя", по ним в дальнейшем будет размещен корабль на доску.
        """
        threedeck_index_lst = []  # сюда будут складываться индексы (палубы) корабля соответствующие индексам доски
        orient = random.randint(0, 1)  # ориентация (0 - горизонтальная, 1 - вертикальная)
        if self.threedeck:  # если 3-х палубник, задан в конструкторе, то ищем индексы где его можно разместить
            starting_point = random.choice(self.index_list)  # стартовая точка, от которой будут строиться палубы
            threedeck_index_lst.append(starting_point)  # добавляем её в список индексов корабля
            # Если ориентация вертикальная ищем 2 свободных индекса над стартоой точкой и добавляем их тот же список:
            if orient and starting_point <= len(self.index_list) - len(self.index_list)/3:
                threedeck_index_lst.append(starting_point + self.size)
                threedeck_index_lst.append(starting_point + (self.size) * 2)
                return threedeck_index_lst  # список с 3-мя индексами будующего корабля
            # Если ориентация вертикальная ищем 2 свободных индекса под стартоой точкой и добавляем их тот же список:
            if orient and starting_point > len(self.index_list) - len(self.index_list)/3:
                threedeck_index_lst.append(starting_point - self.size)
                threedeck_index_lst.append(starting_point - (self.size) * 2)
                return threedeck_index_lst  # список с 3-мя индексами будующего корабля

            if not orient:  # Если ориентация горизонтальная:
                # ищем 2 свободных индекса справа от стартоой точкой и добавляем их тот же список:
                if starting_point+1 in self.index_list:
                    threedeck_index_lst.append(starting_point+1)
                    if starting_point + 2 in self.index_list:
                        threedeck_index_lst.append(starting_point + 2)
                    elif starting_point + 2 not in self.index_list:
                        threedeck_index_lst.append(starting_point - 1)
                    return threedeck_index_lst  # список с 3-мя индексами будующего корабля
                # ищем 2 свободных индекса слева от стартовой точкой и добавляем их тот же список:
                if starting_point+1 not in self.index_list:
                    threedeck_index_lst.append(starting_point - 1)
                    threedeck_index_lst.append(starting_point - 2)
                    return threedeck_index_lst  # список с 3-мя индексами будующего корабля
        if not self.threedeck:  # если 3-х палубный корабль не задан в конструкторе
            return threedeck_index_lst  # вертётся пустой список


    def add_ship_twodeck(self) -> list:
        """
        Метод добавления 2-х палубного корабля на игровое поле. Создан аналогично методу add_ship_threedeck(),
        только в список добавляется не 3, а 2 индекса присущих создаваемому кораблю.

        :return: список с индексами соответствующими "полю боя", по ним в дальнейшем будет размещен корабль на доску.
        """
        twodeck_index_lst = []  # сюда будут складываться индексы (палубы) корабля соответствующие индексам доски
        orient = random.randint(0, 1)  # рандомная ориентация (0 - горизонтальная, 1 - вертикальная)
        if self.twodeck:  # если 2-х палубник задан в конструкторе:
            starting_point = random.choice(self.index_list)  # рандомно выбираем стартовый мндекс из имеющихся в списке
            twodeck_index_lst.append(starting_point)  # помещаем этот индекс в список twodeck_index_lst
            if orient:  # если ориентация вертикальная:
                if starting_point + self.size in self.index_list:  # елси есть свободный индекс под стартовым:
                    twodeck_index_lst.append(starting_point + self.size)  # добавляем его в список twodeck_index_lst
                    return twodeck_index_lst  # возвращаем список индексов корабля
                elif starting_point + self.size not in self.index_list:   # если свободного индекса под стартовым нет:
                    twodeck_index_lst.append(starting_point - self.size)  # берем индекс над стартовым и кладем в список
                    return twodeck_index_lst  # возвращаем список индексов корабля
            elif not orient:   # если ориентация горизонтальная:
                if starting_point + 1 in self.index_list:  # елси есть свободный индекс справа от стартового:
                    twodeck_index_lst.append(starting_point + 1)  # добавляем его в список twodeck_index_lst
                    return twodeck_index_lst  # возвращаем список индексов корабля
                elif starting_point + 1 not in self.index_list:   # елси нет индекса справа от стартового, берем слева:
                    twodeck_index_lst.append(starting_point - 1)  # добавляем его в список twodeck_index_lst
                    return twodeck_index_lst  # возвращаем список индексов корабля

    def add_ship_onedeck(self) -> list:
        """
        Метод добавления однопалубного корабля на игровое поле.
        Выбирается рандомный индекс из имеющихся индексов в списке поля_боя, и помещается в созданный список
        для хранения индекса однопалубника.
        :return: спискок с индексом корабля
        """
        onedeck_index_lst = []  # список для хранения индекса однопалубного корабля
        starting_point = random.choice(self.index_list)  # рандомно выбираем стартовый мндекс из имеющихся в списке
        onedeck_index_lst.append(starting_point)  # добавляем его в список onedeck_index_lst
        return onedeck_index_lst

    def clear_index_list(self, func) -> list:
        """
        метод удаляет индексы будущих кораблей из списка индексов игрового поля, а также индексы вокруг корабля.
        Таким образом при расстановке кораблей будет соблюдена дистанция между ними, т.е. корабли не будут
        наслаиваться друг на друга.
        :param func: принимает функцию, которая возвращает список с индексами корабля.
        :return: None
        """
        index_ship = func()  # текущий список с индексами, которые нужно удалить с поля боя, а также их контурные индексы
        self.ship_list.append(index_ship)  # добавляем этот список в общий список для всех кораблей
        if index_ship:  # если текущий список не пстой:
             for i in index_ship:  # перебераем его по элементам-индексам кораблей
                # далее выполняетя удаление индексов присущим кораблю и его контурных индексов с поля боя
                if i in self.index_list:
                    self.index_list.remove(i)
                if i + self.size in self.index_list:
                    self.index_list.remove(i + self.size)
                if i - self.size in self.index_list:
                    self.index_list.remove(i - self.size)
                if i + self.size + 1 in self.index_list:
                    self.index_list.remove(i + self.size + 1)
                if i + 1 in self.index_list:
                    self.index_list.remove(i + 1)
                if i - self.size + 1 in self.index_list:
                    self.index_list.remove(i - self.size + 1)
                if i - 1 in self.index_list:
                    self.index_list.remove(i - 1)
                if i - self.size - 1 in self.index_list:
                    self.index_list.remove(i - self.size - 1)
                if i + self.size - 1 in self.index_list:
                    self.index_list.remove(i + self.size - 1)


    def get_list_index_ship(self) -> list:
        """
        Метод проверяет вмещаются ли корабли на доску и формирует список индексов, которые в дальнейшем
        займут корабли, если это возможно. В противном случае сообщается об ошибке.
        :return: список с индексами, которыми будет заполнено игровое поле.
        """
        sum_deck = self.onedeck + self.twodeck + self.threedeck  # общее количество палуб
        list_index_ship = []  # сюда будут добавлены индексы каждой палубы всех кораблей
        # бесконечный цикл пока заданое количество палуб больше числа индексов добавляемых в list_index_ship
        while sum_deck > len(list_index_ship):
            # подбираем свободные индексы на поле (клетки которыми будут заняты корабли)
            try:
                for i in range(self.threedeck):  # для каждого 3-х палубного
                    self.clear_index_list(self.add_ship_threedeck)
                for i in range(self.twodeck):  # для каждого 1-х палубного
                    self.clear_index_list(self.add_ship_twodeck)
                for i in range(self.onedeck):  # для каждого однопалубного
                    self.clear_index_list(self.add_ship_onedeck)
            except IndexError:  # если заданое кол-во палуб привышает вместимость на поле боя
                print("Убавьте количество кораблей, они не влезают на поле")
                break
            else:  # если клетка нашлась для каждого корабля
                for i in self.ship_list:  # итерируем общий список со списками индексов кораблей построчно
                    for j in i:           # и каждую строку (т.е. вложеный список) перебераем по элементу
                        list_index_ship.append(j)  # каждый элемент добавляем в ранее созданный list_index_ship
        return list_index_ship  # список клеток (индексов) на поле, которые займут палубы

    def get_template_lists_ships_deck(self) -> list:
        """
        Данныый метод создаёт список, в который входят 3 списка равные кол-ву палуб для 1, 2-х и 3-х палубников"
        Изначально он заполнен нулями, в дальнейшем в него войдут индексы установленных кораблей на поле.
        Например для одного трехпалубника, двух двухпалубных и трёх однопалубных кораблей, он будет таким:

        :return: [[0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] внутренние списки изменяютя в зависимости от кол-ва
        палуб каждого корабля, где размер list[0] = общему числу палуб всех 3-х палубных кораблей,
         размер list[1] = общему числу палуб всех 2-х палубных кораблей, размер list[2] == чмслу однопалубников.
        """
        list_of_ship_lists = []  # пустой список в него будут входить списки равные размерам палуб кораблей
        temp_list = [0]   # временыый список,
        if self.threedeck:  # если есть 3-х палубники:
            temp_list = [0] * 3 * self.threedeck  # увеличиваем temp_list на число всех палуб и кол-во кораблей
            list_of_ship_lists.append(temp_list)  # добавляем получившийся список в общий список
            temp_list = [0]  # после чего возвращаем временный список в прежнее состояние

        # аналогичные действия проводим для 2-х и однопалубных кораблей, если они задагны в конструкторе
        if self.twodeck:
            temp_list = [0] * 2 * self.twodeck
            list_of_ship_lists.append(temp_list)
            temp_list = [0]

        if self.onedeck:
            temp_list = [0] * self.onedeck
            list_of_ship_lists.append(temp_list)

        return list_of_ship_lists  # возвращаем общий собраный общий отсортированый список


class Player:
    def __init__(self):
        self.size = Ship().size  # размер игровой доски
        # данные пользователя:
        self.user_ship_index = self.user_ship_index()     # список с индексами кораблей пользователя
        self.user_field = self.user_field()  # кортеж (игровое поле пользователя заполненное кораблями, список кораблей)
        self.user_sort_deck_lst = Ship().get_template_lists_ships_deck()  # список-шаблон из списков по типу палуб
        # данные компютера:
        self.comp_ship_index = self.comp_ship_index()  # список с индексами кораблей компьютера
        self.comp_field = self.comp_field()  # кортеж: (игровое поле компьютера заполненное кораблями, список кораблей)
        self.comp_sort_deck_lst = Ship().get_template_lists_ships_deck()  # список-шаблон из списков по типу палуб


    def user_ship_index(self):
        """
        :return: метод из класса Ship, возвращающий список с индексами кораблей пользователя
        """
        return Ship().get_list_index_ship()

    def comp_ship_index(self):
        """
        :return: метод из класса Ship, возвращающий список с индексами кораблей компьютера
        """
        return Ship().get_list_index_ship()

    def user_field(self) -> tuple:
        """
        Метод заполняющий игровое поле пользователя кораблями, а так же улучшает визуальное отображение
        перед выводом на экран.
        :return: коржтеж с игровым полем в виде списка заполненного кораблями и списом индесков этих кораблей
        """
        field = GameBoard().change_board()  # пустая игровая доска
        for i in range(len(field)):         # итерируем доску по индексам
            if i in self.user_ship_index:   # если в списке индексов кораблей игрока, встречается такой индекс
                field[i] = chr(11088)      # то присваеваем его элементу, значение = '⭐'
            if field[i] == 0:               # остальное пространство игорового поля, элементы которого равны нулю
                field[i] = chr(127787)      # заполняем значениями =  '🌫'
            if isinstance(field[i], int):   # если в итерируемом поле встречаются цифры:
                field[i] = " " + str(field[i])  # преобразуем их в строки, для нормального отображения на экране
        field[0] = "  "  # первый элемент списка заполняем пробелом, для нормального отображения на экране
        field[size_board - 1] = " " + str(size_board - 1) + " "  # крайнюю координату по горизонтали оборачиваем пробелами
        return field, self.user_ship_index


    def comp_field(self) -> tuple:
        """
        Метод заполняющий игровое поле компьютера кораблями, а так же улучшает визуальное отображение
        перед выводом на экран. Аналог метода user_field(), только для компьютера.
        :return: коржтеж с игровым полем в виде списка заполненного кораблями и списом индесков этих кораблей
        """
        field = GameBoard().change_board()
        for i in range(len(field)):
            if i in self.comp_ship_index:
                field[i] = chr(11088)  # ⭐'
            if field[i] == 0:
                field[i] = chr(127787)  # '🌫'
            if isinstance(field[i], int):
                field[i] = " " + str(field[i])
        field[0] = "  "
        field[size_board - 1] = " " + str(size_board - 1) + " "
        return field, self.comp_ship_index


class GameLogic(Player, GameBoard):


    def error_checking(self, shot: str , dict_cord: dict) -> bool:
        """
        Метод проверяет верно ли пользователь ввёл координаты
        :param shot: строка введенная пользователем
        :param dict_cord: словарь из ключей ввиде строк-координат и значений ввиде индексов на поле
        :return: True если ввод верный
        """
        if shot in dict_cord.keys():  # если введенные данные есть в списке ключей словаря
            return 1  # возвращаем True
        else:
            print("Введены неверные координаты")
            return 0


    def get_sorted_list_deck(self, sort_deck_type_lst: list, ship_index_lst: list) -> list:
        """
        Метод принимает шаблонный список cодержащий три списка из нулей для 3, 2 и 1 - палубных кораблей
        и заполняет эти списки согласно индексам кораблей расставленных на поле.
        Данный метод нужен для того чтобы определить в какой из 3-х видов кораблей мы попали.
        Например: если задан 1 трёхпалубный, 2 двухпалубных и 5 однопалубных кораблей, то получим:
        :param sort_deck_type_lst: [[0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0, 0]] такой шаблон будет на входе
        :param ship_index_lst: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] спискок с индексами кораблей
        :return: [[1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12]]  вернётся такой список с индексами палуб
        """
        cnt = 0  # счётчик, его значение соответствует индексу спмска ship_index_lst
        for i in sort_deck_type_lst:  # итерируем список по подспискам
            for j in range(len(i)):   # итерируем подсписки по их длине
                i.append(ship_index_lst[cnt])  # поочередно добавляем значение из списка ship_index_lst
                cnt += 1   # для этого на каждом шаге увеличиваем значение счётчика на 1
            while 0 in i:  # избавляемся от нулей, которыми изначально заполнись подсписки списка sort_deck_type_lst
                i.remove(0)
        return sort_deck_type_lst  # возвращаем готовый список, из списков с индексами кораблей


    def replace_char(self, lst, index, hit=False):
        """
        Метод меняет значение на игровой доске вы зависимости от попадания. (🔥 - попал, 💦 - промах)
        :param lst: список символизирующий игровое поле
        :param index: индекс, значение которого требуется заменить в списке
        :param hit: булево значение (True - попал, False - мимо), по умолчанию False
        :return: возвращает тот же список, что и принял на вход, с одним измененным значением
        """
        for i in range(len(lst)):     # итерируем список (игровое поле) по индексам
            if hit and i == index:    # Если параметр hit сообщает о выстреле и найден нужный индекс в списке
                lst[i] = chr(128165)  # меняем значение его элемента на 🔥
            if not hit and i == index:   # Если параметр hit сообщает о промахе и найден нужный индекс в списке
                lst[i] = chr(128166)     # меняем значение его элемента на 💦
        return lst  # возвращаем измененный список


    def clear_countur_ship(self, lst_field: list, index: int, lst_ship: list) -> list:
        """
        Метод выполняет замену значений клеток (по индексам) вокруг убитого корабля
        :param lst_field: заполненное игровое поле
        :param index: индекс, вокруг которого заменяются клетки (соседние индексы по кругу)
        :param lst_ship: список индексов всех кораблей
        :return: возвращает игровое поле с изменёнными данными
        """
        index_list = [index+1, index-1, index+self.size,  index-self.size,
                      index+1+self.size, index+1-self.size,
                      index-1+self.size, index-1-self.size]  # список индексов вокруг корабля, которые нужно заменить
        for i in index_list:  # итерируем список индексов находящихся вокруг корабля
            # проверяем каждый из них на принадлежность к игровому полю:
            index_access = [True for _ in range(len(lst_field)) if _ == i]
            # если такой индекс есть на игровой доске, но его нет в списке кораблей, и длина его значения равна 1:
            if index_access and lst_field[i] not in lst_ship and len(lst_field[i]) == 1:
                if lst_field[i] == chr(128165):  # если значение по индексу = 💥
                    lst_field[i] = chr(9989)  # отмечаем что корабль убит "✅"
                else:  # иначе:
                    lst_field[i] = chr(128166)   # меняем значение его элемента на 💦
        lst_field[index] = chr(9989)  # отмечаем что корабль убит "✅"
        return lst_field  # возвращаем изменённое игровое поле

    def request_ship_killed(self, sort_deck_lst: list, index: int) -> bool:
        """
        Метод проверяет убит или ранен корабль с двумя или тремя палубами. Принимает на вход подстреленный индекс
        и список списками индексов живых палуб. Если соседних индексов с текущим не неходит, значит корабль убит.
        :param sort_deck_lst: список из трёх списков, в них хранятся индексы для 3, 2, 1 палубных кораблей.
        :param index: текущий индекс, в который совершено попадание
        :return: булево значение (True - убит, False - не убит)
        """
        if any([index + 1 in sort_deck_lst[1],
                index - 1 in sort_deck_lst[1]]):  # если по горизонтали есть соседний индекс с текущим:
            return False                          # значит корабль не убит, возвращаем False
        elif any([index + self.size in sort_deck_lst[1],
                  index - self.size in sort_deck_lst[1]]):  # если по вертикали есть соседний индекс с текущим:
            return False                                    # значит корабль не убит, возвращаем False
        else:             # иначе
            return True   # корабль уничтожен, возвращаем True

    def add_retired_cord(self, dict_cord: dict, retired_cord: list, index: int, wounded=True) -> list:
        """
        Метод добавляет в список выбывших координат, координаты вокруг убитого корабля
        :param dict_cord: словарь из координат и их индексов на поле
        :param retired_cord: список с выбывшими координатами
        :param index: индекс вокруг которого нужно произвести зачистку
        :param wounded: параметр собщает ранен корабль или убит, по умолчанию ранен True
        :return: дополненный список с выбывшими координатами
        """
        # инвертируем наш словарь наоборот - {индексы: корды}, для обращения к нему по индексам
        inv_dict_cord = {value: key for key, value in dict_cord.items()}

        if wounded:  # если корабль ранен:
            index_list = [index + 1 + self.size, index + 1 - self.size,
                          index - 1 + self.size, index - 1 - self.size]  # список индексов вокруг раненого корабля
            for i in index_list:  # перебераем индексы вокруг убитого корабля
                if i in inv_dict_cord.keys():  # если они встречаются в ключах словаря:
                    retired_cord.append(inv_dict_cord[i])  # добавляем их значения в список с выбывшими координатами
            return retired_cord  # возвращаем дополненный список с выбывшими координатами

        if not wounded:  # если корабль убит:
            index_list = [index + 1, index - 1, index + self.size, index - self.size,
                          index + 1 + self.size, index + 1 - self.size,
                          index - 1 + self.size, index - 1 - self.size]  # список индексов вокруг убитого корабля
            for i in index_list:  # перебераем индексы вокруг убитого корабля
                if i in inv_dict_cord.keys():  # если они встречаются в ключах словаря:
                    retired_cord.append(inv_dict_cord[i])  # добавляем их значения в список с выбывшими координатами
            return retired_cord  # возвращаем дополненный список с выбывшими координатами

        def choice_shot_comp(self, dict_cord: dict, index: int) -> str:
            """
            Метод добивания компьютером раненого корабля
            :param dict_cord: словарь с координатами и индексами
            :param index: индекс раненого корабля
            :return: строку с координатами, по которым будет производиться следующий выстрел
            """
            index_lst = [index + 1, index - 1, index + self.size, index - self.size]  # список возможных целей
            inv_dict_cord = {value: key for key, value in dict_cord.items()}  # инвертируем словарь {значения: ключи}

            while index_lst:       # цикл пока список не пустой
                if not index_lst:  # если индексы в словаре кончились выходим из цикла
                    break
                choice_index = random.choice(index_lst)        # рандомно выбираем один из индексов в списке
                if choice_index not in inv_dict_cord.keys():   # если индекса нет в области индексов поля боя
                    index_lst.remove(choice_index)             # удаляем его из списка
                    continue                                   # и возвращаемся к началу цикла
                elif choice_index in inv_dict_cord.keys():     # если индекс есть в ключах словаря
                    return inv_dict_cord[choice_index]         # возвращаем его значение, т.е. строку координат

class Game(GameLogic):

    def game(self):
        # Данные пользователя:
        user_ship = self.user_field[1]     # список с индексами кораблей пользователя
        user_field = self.user_field[0]    # игровое поле пользователя
        retired_cord_user = []       # сюда будут складываться координаты, по которым уже стрелял пользователь
        count_user = len(user_ship)  # количество жизней (палуб) пользователя
        # Данные компьютера:
        comp_ship = self.comp_field[1]     # список индексов кораблей компьютера
        comp_field = []                    # список будет игровым полем компьютера со скрытыми кораблями
        for i in self.comp_field[0]:       # итерируем заполненное поле компьютера
            if i == chr(11088):           # если встретился элемент '⭐'
                i = chr(127787)            # меняем его значение на '🌫'
            comp_field.append(i)           # каждый элемент поочередно складываем в список comp_field
        retired_cord_comp = []  # сюда будут складываться координаты, по которым уже стрелял компьютер
        count_comp = len(comp_ship)  # количество жизней (палуб) компьютера
        # заполним список, в котором будут храниться индексы кораблей по типу [[3 палубы], [2 палубы], [1 палуба]]
        user_sort_deck_lst = self.get_sorted_list_deck(self.user_sort_deck_lst, comp_ship)  # палубы пользователя
        comp_sort_deck_lst = self.get_sorted_list_deck(self.comp_sort_deck_lst, user_ship)  # палубы компьютера
        dict_cord = self.get_cords()  # словарь {ключи-координаты: значения их индексы на поле}
        who_shot = 1   # чей выстрел (1 - пользователь, 0 - компьютер)

        # НАЧАЛО ИГРЫ:
        self.visual_board(comp_field, user_field)  # выводим доски на экран
        while True:  # бесконечный цикл пока не выполнится одно из условий
            if not count_comp or not dict_cord:  # если все цели компа поражены побеждает пользователь
                print("Вы победили!")
                break
            if not count_user or not dict_cord:  # если все цели пользователя поражены побеждает компьютер
                print("Компьютер победил!")
                break

            if who_shot:  # если стреляет пользователь:
                shot_user = input("Введите корды: ")
                if shot_user == "0":  # выход из игры
                    print("Вы вышли из игры")
                    break
                # если координаты введены неверно, возврат в начало цикла
                if not self.error_checking(shot_user, dict_cord):
                    continue
                elif shot_user in retired_cord_user:  # если введенные координаты уже вводились, возврат в начало цикла
                    print("Вы уже вводили такие координаты")
                    continue
                # если пользователь ввёл верные координаты и они еще не вводились, игра продолжается
                elif self.error_checking(shot_user, dict_cord) and shot_user not in retired_cord_user:
                    retired_cord_user.append(shot_user)  # добавляем их в список выбывших координат пользователя
                    # если в списке кораблей компьютера есть индекс введенных координат:
                    if dict_cord[shot_user] in comp_ship:
                        count_comp -= 1  # уменьшаем кол-во жизней компа на одну
                        # меняем значение на поле компьютера после совершённого выстрела:
                        self.replace_char(comp_field, dict_cord[shot_user], True)  # True указывает на попадание

                        if dict_cord[shot_user] in user_sort_deck_lst[2]:  # если корабль однопалубный:
                            print("Корабль компьютера уничтожен!")
                            # добавляем в список выбывших координат пользователя, контуры убитого корабля:
                            self.add_retired_cord(dict_cord, retired_cord_user, dict_cord[shot_user])
                            # зачищаем игровое поле пользователя вокруг убитого корабля:
                            self.clear_countur_ship(comp_field, dict_cord[shot_user], comp_ship)

                        elif dict_cord[shot_user] in user_sort_deck_lst[1]:  # если корабль двухпалубный:
                            user_sort_deck_lst[1].remove(dict_cord[shot_user])  # удаляем индекс раненого корабля
                            # если двухпалубный корабль компьютера уничтожен:
                            if self.request_ship_killed(user_sort_deck_lst, dict_cord[shot_user]):
                                # добавляем в список выбывших координат пользователя, контуры убитого корабля:
                                self.add_retired_cord(dict_cord, retired_cord_user, dict_cord[shot_user])
                                # зачищаем игровое поле пользователя вокруг убитого корабля:
                                self.clear_countur_ship(comp_field, dict_cord[shot_user], comp_ship)
                                print('Двухпалубный корабль компьютера уничтожен!!!')

                        else:  # если корабль трёхпалубный:
                            user_sort_deck_lst[0].remove(dict_cord[shot_user])  # удаляем индекс раненого корабля
                            if not user_sort_deck_lst[0]:  # если трёхпалубный корабль компьютера уничтожен
                                # добавляем в список выбывших координат пользователя, контуры убитого корабля:
                                self.add_retired_cord(dict_cord, retired_cord_user, dict_cord[shot_user])
                                # зачищаем игровое поле пользователя вокруг убитого корабля:
                                self.clear_countur_ship(comp_field, dict_cord[shot_user], comp_ship)
                                print('Трёхпалубный корабль компьютера уничтожен!!!')

                        self.visual_board(comp_field, user_field)  # выводим доски на экран
                        print("Вы попали в корабль. Следующий ход снова ваш")
                        who_shot = 1  # следующий выстрел пользователя
                        continue      # возвращаемся в начало цикла

                    if dict_cord[shot_user] not in comp_ship:  # если по введенным координатам, корабля нет:
                        # меняем значение на поле компьютера после совершённого выстрела:
                        self.replace_char(comp_field, dict_cord[shot_user])
                        self.visual_board(comp_field, user_field)  # выводим доски на экран
                        print("Вы промахнулись.", end=" ")
                        who_shot = 0  # следующий выстрел компьютера

                ##################################################################################################
                # Условие для добивания корабля ПРИ РАСКОМЕНТИРОВАНИИ ИНОГДА ВЫЛЕТАЕТ ОШИБКА (НУЖНО ДОРАБОТАТЬ!!!)
                # choice_is_made = 0
                # if choice_is_made:  # если стреляет компьютер:
                #     shot_comp = self.choice_shot_comp(dict_cord, dict_cord[shot_comp])
                #     if shot_comp in retired_cord_comp:  # если такие координаты уже использовались:
                #         continue  # возвращаемся в начало цикла
                # if not choice_is_made or shot_comp is None:
                ##################################################################################################

            elif not who_shot:  # если стреляет компьютер:
                # компьютер рандомно выбрает координаты из ключей словаря (с кордами пользователя):
                shot_comp = random.choice([i for i in dict_cord.keys()])
                if shot_comp in retired_cord_comp:    # если такие координаты уже использовались:
                    continue  # возвращаемся в начало цикла
                if shot_comp not in retired_cord_comp:   # если координаты не выбирались ранее:
                    retired_cord_comp.append(shot_comp)  # помещаем их в список выбывших координат компьютера
                    print("Ходит компьютер:", shot_comp)
                    # time.sleep(3)  # имитируем что компьютер думает

                if dict_cord[shot_comp] in user_ship:  # если индекс корд есть в списке кораблей пользователя:
                    count_user -= 1  # уменьшаем кол-во жизней пользователя на одну
                    # меняем значение на поле пользователя после совершённого выстрела:
                    self.replace_char(user_field, dict_cord[shot_comp], True)  # True указывает на попадание

                    if dict_cord[shot_comp] in comp_sort_deck_lst[2]: # если корабль однопалубный:
                        print("Ваш корабль уничтожен!")
                        # добавляем в список выбывших координат компьютера, контуры убитого корабля:
                        self.add_retired_cord(dict_cord, retired_cord_comp, dict_cord[shot_comp])
                        # зачищаем игровое поле компьютера вокруг убитого корабля:
                        self.clear_countur_ship(user_field, dict_cord[shot_comp], user_ship)

                    elif dict_cord[shot_comp] in comp_sort_deck_lst[1]:  # если корабль двухпалубный:
                        comp_sort_deck_lst[1].remove(dict_cord[shot_comp])  # удаляем индекс раненого корабля из списка
                        # добавляем в список выбывших координат компьютера, контуры раненого корабля:
                        self.add_retired_cord(dict_cord, retired_cord_comp, dict_cord[shot_comp], True)  # ранен
                        # choice_is_made = 1  #  добивание корабля (отключен тк. AI не доработан)

                        # если двухпалубный корабль пользователя уничтожен:
                        if self.request_ship_killed(comp_sort_deck_lst, dict_cord[shot_comp]):
                            # добавляем в список выбывших координат компьютера, контуры воуруг убитого корабля:
                            self.add_retired_cord(dict_cord, retired_cord_comp, dict_cord[shot_comp], False)
                            # зачищаем игровое поле пользователя вокруг убитого корабля:
                            self.clear_countur_ship(user_field, dict_cord[shot_comp], user_ship)
                            print('Ваш двухпалубный корабль уничтожен!!!')

                    else:  # если корабль трёхпалубный:
                        comp_sort_deck_lst[0].remove(dict_cord[shot_comp])  # удаляем индекс раненого корабля из списка
                        # добавляем в список выбывших координат компьютера, контуры раненого корабля:
                        self.add_retired_cord(dict_cord, retired_cord_comp, dict_cord[shot_comp], True)  # ранен
                        # choice_is_made = 1  #  добивание корабля (отключен тк. AI не доработан)

                        if not comp_sort_deck_lst[0]:   # если трёхпалубный корабль пользователя уничтожен
                            # добавляем в список выбывших координат пользователя, контуры убитого корабля:
                            self.add_retired_cord(dict_cord, retired_cord_comp, dict_cord[shot_comp], False)
                            # зачищаем игровое поле пользователя вокруг убитого корабля:
                            self.clear_countur_ship(user_field, dict_cord[shot_comp], user_ship)
                            print('Ваш трёхпалубный корабль уничтожен!!!')

                    self.visual_board(comp_field, user_field)  # выводим доски на экран
                    print("Компьютер попал в корабль.", end=" ")
                    # time.sleep(3)  # имитируем что компьютер думает
                    who_shot = 0    # следующий выстрел компьютера
                    continue  # возврат в начало цикла
                if dict_cord[shot_comp] not in user_ship:  # если промах производим аналогичные операции
                    # меняем значение на поле пользователя после совершённого выстрела:
                    self.replace_char(user_field, dict_cord[shot_comp])
                    self.visual_board(comp_field, user_field)  # выводим доски на экран
                    print("Компьютер промахнулся. Ваш ход")
                    who_shot = 1  # следующий выстрел пользователя
                    # choice_is_made = 0  # параметр  добивание корабля (отключен тк. AI не доработан)

    def start_game(self):
        print("Добро пожаловать в игру Морской Бой! \nВыбирите один из пунктов меню.")
        print('1 - Приступить к игре')
        print('2 - Информация о проекте')
        print('0 - Выход из программы в любой момент игры')
        while True:
            choice = int(input("Введите с клавиатуры 1, 2 или 0: "))
            if int(choice) == 0:
                print("Вы вышли из игры")
                break
            if choice == 1:
                print('Вы выбрали игру правила стандартные, описывать не буду')
                print("Формат ввода координат - 12, где 1 - вертикаль, 2 - горизонталь ")
                time.sleep(5)
                self.game()
            if choice == 2:
                with open('info.txt', 'r', encoding='utf8') as f:
                    # в данном блоке с файлом можно работать:
                    print(f.read())



if __name__ == '__main__':  # запуск программы
    g = Game()
    g.start_game()

