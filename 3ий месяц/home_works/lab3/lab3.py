from dataclasses import field
from random import randint
class Field:
    def __init__(self, field_size: int = 3) -> None:
        self.field_size = field_size
        self.playing_field = []
        for _ in range(field_size):
            self.playing_field.append([None] * field_size) # [None, None, None]
        self.free_cells = field_size ** 2

    def field_is_occupied(self, x: int, y: int):
        return self.playing_field[x][y]

    def __checking_coordinates(self, x: int, y: int):
        if x > self.field_size - 1 or y > self.field_size - 1 or x < 0 or y < 0:
            raise ValueError(f"Координата ({x}, {y}) находится вне поля")
        if self.field_is_occupied(x, y):
            raise ValueError(f'Ячейка ({x},{y}) занята')

    def set_value(self, x: int, y: int, char: str):
        self.__checking_coordinates(x, y)
        self.playing_field[x][y] = char
        self.free_cells -= 1

    def display(self):
        print(' ' * 3, end='|')
        for i in range(self.field_size):
            print(f"{i:^3}", end='|')
        print()
        for i in range(self.field_size):
            result_row = f"{i:^3}|"
            value_list = list(map(lambda v: f"{v or '':^3}", self.playing_field[i]))
            result_row += '|'.join(value_list)
            result_row +="|"
            print('-' * len(result_row))
            print(result_row)


class Player:
    def __init__(self, char: str, field: Field) -> None:
        self.char = char
        self.field = field

    def _get_coordinates(self):
        while True:
            try:
                x = int(input("Введите координату x: "))
                y = int(input("Введите координату y: "))
                return x, y
            except ValueError:
                print("Введите числа")

    def make_move(self):
        while True:
            try:
                x, y = self._get_coordinates()
                self.field.set_value(x, y, self.char)
                break
            except ValueError as e:
                print(e)


class Bot(Player):
    def _get_coordinates(self):
        while True:
            x = randint(0, self.field.field_size - 1)
            y = randint(0, self.field.field_size - 1)
            if not self.field.field_is_occupied(x, y):

                return x, y

class Checker():
    def __init__(self, field: Field) -> None:
        self.field = field

    def check_win(self, char: str):
        fieldForChecking = []
        for each in self.field.playing_field:
            field_elem = []
            for i in range(len(each)):
                field_elem.append(each[i])
            fieldForChecking.append(field_elem)

        for each in fieldForChecking:
            for i in range(len(each)):
                if each[i] != char:
                    each[i] = None

        win_cords = (
        ([char, None, None], [None, char, None], [None, None, char]), 
        ([None, None, char], [None, char, None], [char, None, None]), 

        ([char, char, char], [None, None, None], [None, None, None]), 
        ([None, None, None], [char, char, char], [None, None, None]), 
        ([None, None, None], [None, None, None], [char, char, char]),

        ([char, None, None], [char, None, None], [char, None, None]),
        ([None, char, None], [None, char, None], [None, char, None]),
        ([None, None, char], [None, None, char], [None, None, char]),
        )

        for i in range(len(win_cords)):
            winOrNot = 0
            for j in range(len(win_cords[i])):
                if win_cords[i][j] == fieldForChecking[j]:
                    winOrNot += 1
            if winOrNot == self.field.field_size:
                return True
        return False

class Game():
    def __init__(self, field: Field) -> None:
        self.field = field

    def one_more_game(self, text):
        confirm = input(text).lower()
        if confirm in ("yes", "да", "конечно"):
            return True
        else:
            return False
        
    def full(self):
        count = 0
        for i in range(len(self.field.playing_field)):
            if None not in self.field.playing_field[i]:
                count += 1

        if count == 3:
            self.main()

    def main(self):
            print("Введите exit для того что бы выйти")
            gameMode = input("Выбор режима игры(1 или 2): ").lower()
            if gameMode == "1":
                player_1 = Player('x', self.field)
                player_2 = Bot('o', self.field)
                checker = Checker(self.field)

                def quie1():
                    player_1.make_move()
                    field_1.display()
                    print("*" * 40)
                    player_2.make_move()
                    field_1.display()
                
                def quie2():
                    player_2.make_move()
                    field_1.display()
                    print("*" * 40)
                    player_1.make_move()
                    field_1.display()
                quie = randint(1, 2)

                while True:
                    if quie == 1:
                        quie1()
                    else:
                        quie2()

                    if checker.check_win("x") == True:
                        print("Поздравляем вы победили")
                        if self.one_more_game("Вы хотите сыграть еще?"):
                            self.main()
                        else:
                            break

                    if checker.check_win("o") == True:
                        print("К сожалению вы проиграли")
                        if self.one_more_game("Вы хотите сыграть еще?"):
                            self.main()
                        else:
                            break
                    
                    self.full()

            elif gameMode == "2":
                player_1 = Player('x', self.field)
                player_2 = Player('o', self.field)
                checker = Checker(self.field)
                
                while True:
                    player_1.make_move()
                    if checker.check_win("x") == True:
                        print("Первый игрок победил")
                        if self.one_more_game("Вы хотите сыграть еще?"):
                            self.main()
                        else:
                            break
                    field_1.display()
                    print("*" * 40)
                    player_2.make_move()
                    if checker.check_win("o") == True:
                        print("второй игрок победил")
                        if self.one_more_game("Вы хотите сыграть еще?"):
                            self.main()
                        else:
                            break
                    field_1.display()

                    self.full()
            elif gameMode == "exit":
                exit()
            else: 
                print("Попробуйте вновь")
                self.main()


field_1 = Field()
game = Game(field_1)
game.main()