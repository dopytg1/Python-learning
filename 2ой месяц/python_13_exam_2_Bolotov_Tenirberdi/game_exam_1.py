import random

robot = {
    'hp': 1300,     
    'defence': 120,   
    'gun': 300,       	
    'name': "Robot"
}
hero = {
    'hp': 2000,
    'defence': 100, #Also don't forget to change the remove_shield option
    'gun': 250,
    'protective_field': 150,    
    'name': "Hero",
    'has_shield': False,
    'adrenalin': 1
}
myList = [1, 2, 3, 4, 5]

for i in range(len(myList)):
    print(myList[i])

for i, b in hero.items():
    print(i) 


def display_robot_info():
    print("Robot's hp: %s" %(robot['hp']))


def display_hero_info():
    print("Hero's hp: %s" %(hero['hp'])) 
    if hero['has_shield']:               #Checking if shild is open or not
        print("Shield is: on")
    else:
        print("Shield is: off")
    print("adrenaline left: %s" %(hero['adrenalin']))


def modify_health(char, dmg):
    dmg = dmg * -1
    char['hp'] = char['hp'] + dmg
    print("The %s recieved %s units of hp" %(char['name'], dmg))


def hero_attack():
    hit_probability = random.randint(1, 100)

    if hit_probability >= 25:
        damage = hero['gun'] - robot['defence']
        print("You fired the robot with a gun")
        modify_health(robot, damage)
    else:
        print("You missed")


def equip_shield():
    hero['has_shield'] = True
    

def remove_shield():
    hero['has_shield'] = False
    if hero['defence'] != 100:
        hero['defence'] = hero['defence'] - hero['protective_field']


def hero_defence():
    print("Hero is under shield")
    equip_shield()
    hero['defence'] = hero['defence'] + hero['protective_field']


def hero_healing():
    if hero['adrenalin'] > 0:
        modify_health(hero, -500)
        hero['adrenalin'] = hero['adrenalin'] - 1
    else:
        print("You have no adrenalin left")
        hero_turn()


def hero_turn():
    player_move = input("Do you wanna attack, pass, defence or heal? ")
    print(" ")

    if player_move == "attack":
       hero_attack()
    elif player_move == "defence":
        hero_defence()
    elif player_move == 'heal':         #Hero using adrenalin
        hero_healing()
    elif player_move == "pass":
        pass
    else:
        print("Try again")
        hero_turn()


def robot_homing_missile():
    print("\nRobot launched the homing missile!!! ")
    damage = (robot['gun'] + (robot['gun'] * 0.3)) - hero['defence']
    modify_health(hero, damage)
        

def robot_gun():
    hitOrNot = random.randint(1, 2)
    if hitOrNot == 1:
        print("\nRobot fired with a gun")
        damage = robot['gun'] - hero['defence']
        modify_health(hero, damage)
    else:
        print("\nRobot missed")


def robot_poison_grenade():
    print("The robot threw a poison grenade!!!!")
    if not hero['has_shield']:
        damage = robot['gun'] * 2
        modify_health(hero, damage)
    else:
        print("Your defence did great. ")
        pass

def robot_turn():
    randNum = random.randint(1, 4) # Robot attack types

    if randNum == 1:
        robot_homing_missile()
    elif randNum == 2:
        robot_gun()
    elif randNum == 3:
        robot_poison_grenade()
    else:
        print("\nRobot jammed")


i = 0  # adding the reference point

# while True:
#     print("*" * 50) # adding this for a better look
#     print(" ")

#     hero_turn()

#     if robot['hp'] <= 0:
#         print("CONGRATS!!! HERO WON THE BATTLE \nTotal: %s moves" %i)
#         break

#     print(" ")

#     robot_turn()
#     if hero['hp'] <= 0:
#         print("Unfortunately, Robot won. Maybe next time \nTotal: %s moves" %i)
#         break

#     # Printing the stats of players
#     print(" ")
#     display_robot_info()
#     print(" ")
#     display_hero_info()

#     remove_shield()
    
#     i += 1