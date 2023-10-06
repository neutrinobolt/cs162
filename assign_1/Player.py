
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