"""File contains Combatant-based classes. """

import items

class Combatant:
    """Parent class for all combatants."""

    def __init__(self,
                 name,
                 elem_type,
                 level,
                 hp_max,
                 def_skill,
                 armor_equipped: list,
                 inventory:list):
        
        #Directly derived from params
        self.name = name
        self.elem_type = elem_type
        self.level = level
        self.hp_max = hp_max
        self.def_skill = def_skill
        self.armor_equipped = armor_equipped
        self.inventory = inventory

        self.opponent = None

    def find_opponent(self,
                      opponent: lambda: Combatant):
        """Select another entity of class Combatant as opponent."""

        self.opponent = opponent



class Player(Combatant):
    """Initializes player class."""
    def __init__(self,
                 name = "No name",
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
                 inventory:list = []):
        
        #It was at this moment, after typing out that whole mess, that I
        #realized I may have bitten off more than I could chew.

        super().__init__(name,
                       elem_type,
                       level,
                       hp_max,
                       def_skill,
                       armor_equipped,
                       inventory)

        self.xp = xp_current
        self.hp_current = hp_max
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

    def __str__(self):
        """This should print out all the relevant stats connected to 
        the player. PV is included for file storage."""
        return  f"{self.name}:\n\n" \
                f"\tType: {self.elem_type}\n" \
                f"\tLevel {self.level}\n" \
                f"\tXP: {self.xp}\n" \
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
                f"\tType: {self.elem_type}\n" \
                f"\tXP: {self.xp}/50\n" \
                f"\tHP:{self.skills[0]}/{self.hp_current}\n" \
                f"\tDefense:{self.skills[1]}\n\n" \
                f"\tSword Skill:{self.skills[2]}\n" \
                f"\tAxe Skill:{self.skills[3]}\n" \
                f"\tSpear Skill:{self.skills[4]}\n" \
                f"\tDagger Skill:{self.skills[5]}\n" \
                f"\tBow Skill:{self.skills[6]}\n" \
                
    def view_inventory(self) -> str:
        "Prints a list of inventory contents."

        result = ""
        for item in self.inventory:
            result += f"\t{item}\n"
        return  "Current Inventory:\n" \
                f"{result}"

    def obtain(self, item: items.Weapon):
        """Adds given item to player inventory."""
        self.inventory.append(item.name())

    

    def attack(self):
        pass

class Enemy(Combatant):
    """Initializes Enemy class."""

    def __init__(self,
                 name= "No name",
                 elem_type = "water",
                 level = 1,
                 hp_max = 10,
                 def_skill = 1,
                 armor_equipped: list = [],
                 inventory: list = [],#values to super
                 ):
    
        super().__init__(name=name,
                         elem_type=elem_type,
                         level=level,
                         hp_max=hp_max,
                         def_skill=def_skill,
                         armor_equipped=armor_equipped,
                         inventory=inventory)
        
        def attack(self):
            pass

        def drop(self):
            pass
