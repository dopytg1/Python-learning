from cgi import print_arguments
from random import randint
import time

class EquipmentWornOutError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class FreeSlotError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class TotalVolumeError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Equipment():
    def __init__(self, taken_capacity: int, name: str, wear_condition: int = 0):
        self.wear_condition = wear_condition
        self.taken_capacity = taken_capacity
        self.name = name
        self.validation()

    def validation(self):
        if self.taken_capacity not in range(30, 101):
            raise ValueError("Переданное значение не входит в диапазон между 30 и 100")

    def action(self):
        if self.wear_condition >= 100:
            raise EquipmentWornOutError("Оружие изношено")
        else:
            self.wear_condition += 10

    def value_with_condition(self, value: int):
        if self.wear_condition == 0:
            return value 
        elif self.wear_condition > 100:
            print("Экипировка сломана")
            return 0
        else:
            return value - value * self.wear_condition / 100

    def print_equip(self):
        print(f"name: {self.name:<20}\nWear condition: {self.wear_condition}")
        
class Weapon(Equipment):
    def __init__(self, taken_capacity:int, name:str, min_damage: int, critical_hit_chance: int, wear_condition=0,):
        self.min_damage = min_damage
        self.max_damage = int(self.min_damage + self.min_damage * 0.4)
        self.critical_hit_chance = critical_hit_chance
        super().__init__(taken_capacity, name, wear_condition)
        self.validation()

    def validation(self):
        if self.min_damage not in range(5, 101):
            raise ValueError("Не в диапазоне: минимальный наносимый урон (от 5 до 40)")
        if self.critical_hit_chance not in range(1, 71):
            raise ValueError("Не в диапазоне: шанс критического урона (от 1 до 70)")
        super().validation()

    def action(self):
        super().action()
        if randint(1, 100) <= 15:
            return 0
        else:
            if randint(1, 100) <= self.critical_hit_chance:
                return self.value_with_condition(int(self.max_damage + self.max_damage * 0.4))
            else:
                return self.value_with_condition(randint(self.min_damage, self.max_damage))

    def print_weapon(self):
        super().print_equip()
        print(f"Min damage: {self.min_damage}\nMax damage: {self.max_damage}\nCritical hit chance: {self.critical_hit_chance}")

class Armor(Equipment):
    def __init__(self, taken_capacity: int, name: str, defence: int, wear_condition: int = 0):
        self.defence = defence
        super().__init__(taken_capacity, name, wear_condition)
        self.validation()

    def validation(self):
        if self.defence not in range(1, 11):
            raise ValueError("Не в диапазоне: количество единиц защиты (от 1 до 10)")
        super().validation()

    def action(self):
        super().action()
        return self.value_with_condition(self.defence)

    def print_armor(self):
        super().print_equip()
        print(f"Defence: {self.defence}")

class Navigator(Equipment):
    def __init__(self, taken_capacity: int, name: str, accuracy: int, wear_condition: int = 0):
        self.accuracy = accuracy 
        super().__init__(taken_capacity, name, wear_condition)
        self.validation()

    def validation(self):
        if self.accuracy not in range(5, 41):
            raise ValueError("Не в диапазоне: количество единиц точности(от 5 до 40)")
        super().validation()

    def action(self):
        super().action()
        if randint(1, 100) < 20:
            return self.value_with_condition(int(self.accuracy / 2))
        else:
            return self.value_with_condition(self.accuracy)


    def print_navigation(self):
        super().print_equip()
        print(f"Accuracy: {self.accuracy}")


class Spaceship():
    def __init__(self, name, spaciousness: int, accuracy, health = 1000 ):
        self.name = name
        self.spaciousness = {"max_spaciousness": spaciousness, "spaciousness": 0}
        self.accuracy = accuracy
        self.health = health
        self.equiped_weapons = []
        self.equiped_armors = []
        self.equiped_navigators = []
        self.validation()

    def validation(self):
        if self.accuracy not in range(0, 6):
            raise ValueError("Не в диапазоне: диапазон базовой точности корабля(от 0 до 5)")

    def equip_weapon(self, weapon: Weapon):
        if len(self.equiped_weapons) < 4 and self.spaciousness['spaciousness'] + weapon.taken_capacity < self.spaciousness['max_spaciousness']:
            self.equiped_weapons.append(weapon)
            self.spaciousness['spaciousness'] += weapon.taken_capacity
        elif len(self.equiped_weapons) >= 4 and self.spaciousness['spaciousness']:
            raise FreeSlotError("нет свободных слотов")
        elif self.spaciousness['spaciousness'] + weapon.taken_capacity > self.spaciousness['max_spaciousness']:
            raise TotalVolumeError("обьем помещенных слотов превышен")

    def equip_armor(self, armor: Armor):
        if len(self.equiped_armors) < 3 and self.spaciousness['spaciousness'] + armor.taken_capacity < self.spaciousness['max_spaciousness']:
            self.equiped_armors.append(armor)
            self.spaciousness['spaciousness'] += armor.taken_capacity
        elif len(self.equiped_armors) >= 3 and self.spaciousness['spaciousness']:
            raise FreeSlotError("нет свободных слотов")
        elif self.spaciousness['spaciousness'] + armor.taken_capacity > self.spaciousness['max_spaciousness']:
            raise TotalVolumeError("обьем помещенных слотов превышен")

    def equip_navigator(self, navigator: Navigator):
        if len(self.equiped_navigators) < 4 and self.spaciousness['spaciousness'] + navigator.taken_capacity < self.spaciousness['max_spaciousness']:
            self.equiped_navigators.append(navigator)
            self.spaciousness['spaciousness'] += navigator.taken_capacity
        elif len(self.equiped_navigators) >= 4 and self.spaciousness['spaciousness']:
            raise FreeSlotError("нет свободных слотов")
        elif self.spaciousness['spaciousness'] + navigator.taken_capacity > self.spaciousness['max_spaciousness']:
            raise TotalVolumeError("обьем помещенных слотов превышен")


    def attack(self, attacked_ship):
        total_accuracy = self.accuracy
        for each in self.equiped_navigators:
            try:
                total_accuracy += each.action()
            except EquipmentWornOutError:
                self.equiped_navigators.remove(each)
        if total_accuracy > 100:
            total_accuracy = 100

        for each in self.equiped_weapons:
            if randint(1, 100) < total_accuracy:
                try:
                    self.defend(each.action(), attacked_ship)
                except EquipmentWornOutError:
                    self.equiped_weapons.remove(each)
    

    def defend(self, damage, attacked_ship):
        if len(self.equiped_armors) != 0:
            self_defence = int((1 / (self.spaciousness['max_spaciousness'] *  len(self.equiped_armors))) * 10 ** 4)
        else:
            self_defence = 10
        total_def = self_defence
        for each in attacked_ship.equiped_armors:
            try:
                total_def += each.action()
            except EquipmentWornOutError:
                attacked_ship.equiped_armors.remove(each)

        final_damage = int(damage) - int(total_def)
        if final_damage > 0:
            attacked_ship.health -= final_damage

    def print_ship(self):
        print(f"Ship name: {self.name:}\nShip spaciousness: {self.spaciousness['max_spaciousness']}\nShip health: {self.health}")
        print(f"Amount of ship weapons: {len(self.equiped_weapons)}\nAmount of ship armors: {len(self.equiped_armors)}\nAmount of ship navigators: {len(self.equiped_navigators)}")
        print("*" * 40)

class Aplication():

    def createListOfEquips(self):
        equipments = []
        for _ in range(20):
            randEquips = randint(1,3)
            if randEquips == 1:
                randArgCapacity = randint(30, 100)
                randArgMinDamage = randint(5, 40)
                randCriticalDamage = randint(1, 70)
                weapon = Weapon(randArgCapacity, "weapon", randArgMinDamage, randCriticalDamage)
                equipments.append(weapon)
            elif randEquips == 2:
                randArgCapacity = randint(30, 100)
                randDefence = randint(1, 10)
                armor = Armor(randArgCapacity, "armor", randDefence)
                equipments.append(armor)
            elif randEquips == 3:
                randArgCapacity = randint(30, 100)
                randAccuracy = randint(10, 40)
                navigator = Navigator(randArgCapacity, "navigator", randAccuracy)
                equipments.append(navigator)
        
        return equipments
        
    def createShips(self):
        ships = []
        for _ in range(2):
            spaciousness = randint(300, 1000)
            accuracy = randint(0, 5)
            ship = Spaceship("spaceship", spaciousness, accuracy)
            ships.append(ship)

        return ships

    def fillShips(self):
        ships = self.createShips()
        equipments = self.createListOfEquips()

        for ship in ships:
            for each in equipments:
                try:
                    if isinstance(each, Weapon):
                        ship.equip_weapon(each)
                        equipments.remove(each)
                    if isinstance(each, Armor):
                        ship.equip_armor(each)
                        equipments.remove(each)
                    if isinstance(each, Navigator):
                        ship.equip_navigator(each)
                        equipments.remove(each)
                except:
                    continue
        
        print(ships[0].attack(ships[1]))
        for each in ships[0].equiped_weapons:
            print(each.action())
        print(ships[0].equiped_weapons)
        return ships

    def main(self):
        ship1, ship2 = self.fillShips()
        i = 0
        while i < 20:
            print(f"Раунд номер: {i + 1}")

            # First ship turn
            print(f"Первый корабль атакует")
            ship1.attack(ship2)
            print("*" * 40)
            print("Второй корабль:")
            print(ship2.print_ship())

            # Second ship turn 
            print(f"Второй корабль атакует")
            ship2.attack(ship1)
            print("*" * 40)
            print("Первый корабль:")

            print(ship1.print_ship())
            
            i += 1

            if ship1.health < 0:
                print("Победил второй корабль")
                break
            if ship2.health < 0:
                print("Победил первый корабль")
                break

        if ship1.health > ship2.health:
            print("Победил первый корабль")
        elif ship1.health < ship2.health:
            print("Победил второй корабль")

        anotherPlay = input("хотите сыграть еще(да или нет): ")
        if anotherPlay == "да":
            self.main()

        
app = Aplication()
app.main()
app.fillShips()