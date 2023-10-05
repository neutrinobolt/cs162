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

class Player:

    def __init__(self,
                 name = "Player",
                 elem_type = "Water",
                 level = 1,
                 hp_max = 10,
                 def_skill = 1,
                 sword_skill = 1,
                 axe_skill = 1,
                 spear_skill = 1,
                 dagger_skill = 1,
                 bow_skill = 1,
                 xp_current = 0,
                 hp_pv = 0,
                 def_pv = 0,
                 sword_pv = 0,
                 axe_pv = 0,
                 spear_pv = 0,
                 dagger_pv = 0,
                 bow_pv = 0,
                 armor_equipped: list = [],
                 inventory: list = [] ): 
        #It was at this moment, after typing out that whole mess, that I 
        #realized I may have bitten off more than I could chew.
        self.name = name
        self.type = elem_type
        self.level = level
        self.xp = xp_current
        self.skills = [hp_max,
                       def_skill,
                       sword_skill,
                       axe_skill,
                       spear_skill,
                       dagger_skill,
                       bow_skill]
        self.pvs = [
            hp_pv,
            def_pv,
            sword_pv,
            axe_pv,
            spear_pv,
            dagger_pv,
            bow_pv]
        self.armor = armor_equipped
        self.inventory = inventory

    def __str__(self):
        """This should print out all the relevant stats connected to 
        the player. PV is included for development sake.\t"""
        return  f"{self.name}\n\n" \
                f"\tType: {self.type}\n" \
                f"\tLevel {self.level}\n" \
                f"\tXP: {self.xp} out of 50\n" \
                f"\tHP:{self.skills[0]}\n" \
                f"\tHP PV:{self.pvs[0]}\n" \
                f"\tDefense:{self.skills[1]}\n" \
                f"\tDefense PV:{self.pvs[1]}\n" \
                f"\tSword Skill:{self.skills[2]}\n" \
                f"\tAxe Skill:{self.skills[3]}\n" \
                f"\tSpear Skill:{self.skills[4]}\n" \
                f"\tDagger Skill:{self.skills[5]}\n" \
                f"\tBow Skill:{self.skills[6]}\n" \
                f"\tSword PV:{self.pvs[2]}\n" \
                f"\tAxe PV:{self.pvs[3]}\n" \
                f"\tSpear PV:{self.pvs[4]}\n" \
                f"\tDagger PV:{self.pvs[5]}\n" \
                f"\tBow PV:{self.pvs[6]}\n" \
                f"\tInventory:\n\t{self.inventory}"
    
    def view_stats(self) -> str:
        """Prints stats for player use. Hence PV's are removed."""
        return  f"Stats of {self.name}:\n\n" \
                f"\tLevel {self.level}\n" \
                f"\tType: {self.type}\n" \
                f"\tXP: {self.xp} out of 50\n" \
                f"\tHP:{self.skills[0]}\n" \
                f"\tDefense:{self.skills[1]}\n\n" \
                f"\tSword Skill:{self.skills[2]}\n" \
                f"\tAxe Skill:{self.skills[3]}\n" \
                f"\tSpear Skill:{self.skills[4]}\n" \
                f"\tDagger Skill:{self.skills[5]}\n" \
                f"\tBow Skill:{self.skills[6]}\n" \
                
    def view_inventory(self) -> str:
        "Prints a list of inventory contents."

        inventory_pretty = ""
        for item in self.inventory:
            inventory_pretty += f"\t{item}\n"
        return  "Current Inventory:\n" \
                f"{inventory_pretty}"

        
    
    def obtain(self, item: str):
        """Adds given item to player inventory."""
        self.inventory.append(item)

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
