"""
# Ben Snider, CS162, 10.3.2023
This assignment is already late, so I'll keep this short. 
The file combatant_test.py located in this folder should contain the combatant
class structure as described in my Google doc, then create create a level 1, water type instance
named "Player" within the code. Then, it will ask the user to name "Player".
At LVL 1 all used stats should just be set to 1, except for HP which starts at 10, and PV's 
and XP start at 0. 
After naming the character they will be given the choice between 2 of the 5 possible weapon
types to be their starting weapon, and on deciding they will be given a wooden version
(base attack 1) of that weapon type sent to their inventory. 
The program will then give them the option to 
view their current stats (excluding PV's) and inventory, or to end the program."""
# Create combatant class

import random
from Player import Player

#Get character name from user, initialize player
loop = 1
while loop == 1:
    try:
        chosen_name = input("Please enter your character's name " \
                            "(may not exceed 16 characters):\n")
        if len(chosen_name) > 10:
            print("ERROR, name is too long.")
        else:
            loop = 0
    except:
        print("ERROR, something went wrong. Please try again.")

new_player = Player(name = chosen_name)
#print(new_player.view_stats())

#Offer 2 randomly selected wooden forms of each weapon type for starting weapon

starting_weapons = ["Wooden Sword",
                    "Wooden Axe",
                    "Wooden Spear",
                    "Wooden Dagger",
                    "Wooden Bow"]
open_selection = random.sample(starting_weapons, 2)
#print(open_selection)

print("Please choose your starting weapon:")
select_num = 0
weapon_spread = []
for option in open_selection:
    print(f"{select_num}: {option}")
    select_num +=1
    weapon_spread.append(option)

loop = 1
while loop == 1:
    try:
        player_decision = int(input())
    except ValueError:
        print("ERROR, invalid input. Please try again:")
    except:
        print("ERROR, something unexpected occurred. Please try again:")
    if player_decision <= 1:
        new_player.obtain(weapon_spread[player_decision])
        loop = 0
    else:
        print("ERROR, invalid input. Please try again:")

#Allow user to either view stats, view inventory, or exit program.



loop = 1
while loop == 1:
    print("-" * 50)
    print(f"Main Menu\n\t0: exit \n\t1: View inventory\n\t2:view {chosen_name}'s stats")    
    try:
        player_decision = int(input())
    except ValueError:
        print("ERROR, invalid input. Please try again:")
    except:
        print("ERROR, something unexpected occurred. Please try again:")
    if player_decision <= 2:
        if player_decision == 0:
            loop = 0
        elif player_decision == 1:
            print(new_player.view_inventory())
            input("Press enter to return to Main Menu")
        elif player_decision == 2:
            print(new_player.view_stats())
            input("Press enter to return to Main Menu")

    else:
        print("ERROR, invalid input. Please try again:")
