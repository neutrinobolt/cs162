"""File contains Item-based classes."""

class Weapon():
    """Initializes Weapon class."""

    def __init__(self,
                 element = None,
                 power = "wooden",
                 w_type = "sword",
                 durability = 20
                 ):

        #Set up name parts
        self.element = element

        self.powers = {"wooden": 2,
                       "stone": 5}
        self.power = self.powers[power]
        self.power_name = power
        self.w_types = ["sword",
                        "axe",
                        "spear",
                        "dagger",
                        "bow"]
        self.w_type = w_type

       

        self.durability = durability

    def name(self) -> str :
        """Returns the name of the item."""

         #Create name
        if self.element is None:
            name = f"{self.power_name} {self.w_type}"
        else:
            name = f"{self.power_name} {self.element} {self.w_type}"

        return name
        