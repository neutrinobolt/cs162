"""Main driver for final project. 

Final result will: 
-Open welcome screen and allow to either start new game or load previous one, 
if it exists
-Enter player into combat with golems of randomly generated level and elem type
"""

import combatants
import items

def main():
    pc = combatants.Player()
    start_weapon = items.Weapon()
    pc.obtain(start_weapon)
    print(pc.view_stats())

if __name__ == "__main__":
    main()
