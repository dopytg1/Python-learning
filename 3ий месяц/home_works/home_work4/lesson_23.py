from random import randint
class Field:
    def __init__(self, field_size: int = 3) -> None:
        self.field_size = field_size
        # self.playing_field = [[None]* field_size for _ in range(field_size)]
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

f = Field()
# f.display()
# f.set_value(1, 2, 'o')
# f.set_value(0, 2, 'x')
# f.display()
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

# field_1 = Field()
# player_1 = Player('o', field_1)
# player_2 = Bot('x', field_1)
# while True:
#     player_1.make_move()
#     field_1.display()
#     player_2.make_move()
#     field_1.display()
char = 'x'
field_1 = Field()
field_1.set_value(0,1, char)
field_1.set_value(1,1, char)
field_1.set_value(2,1, char)
field_1.display()

# for i in range(len(field_1.playing_field)):
#     is_win = True
#     for j in range(len(field_1.playing_field)):
#         if field_1.playing_field[i][j] != char:
#             is_win = False
#             break
#     if is_win:
#         print('win')

for i in range(len(field_1.playing_field)):
    is_win = True
    for j in range(len(field_1.playing_field)):
        if field_1.playing_field[j][i] != char:
            is_win = False
            break
    if is_win:
        print('win')

for i in range(len(field_1.playing_field)):
    is_win = True
    if field_1.playing_field[i][i] != char:
        is_win = False
        break
if is_win:
    print('win')