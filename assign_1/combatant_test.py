# Create combatant class

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

        def __str__():
            """not looking for pretty at this point, just functional. Not winning
            a bestseller or anything with this code."""
            return  f"{self.name}\n\n" \
                    f"Level {self.level}\n" \
                    f"HP:{self.skills[hp_max]}\n" \
                    f"Defense:{self.skills[def_skill]}\n" \
                    f"Sword Skill:{self.skills[sword_skill]}\n" \
                    f"Axe Skill:{self.skills[axe_skill]}\n" \
                    f"Spear Skill:{self.skills[spear_skill]}\n" \
                    f"Dagger Skill:{self.skills[dagger_skill]}\n" \
                    f"Bow Skill:{self.skills[bow_skill]}\n" \
                    f"Inventory:\n\t{self.inventory}"
