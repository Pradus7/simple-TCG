class Card:
    def __init__(self, id, name="", cost=0, damage=0, health=1):
        """
        A Card class that defines the properties of a card
            id: a card id used to identify the card
            name: the name that is displayed on the card
            cost: the cost it takes to play the card
            damage: the card's current attack damage value
            initDmg: the card's original attack damage
            health: the card's current health value
            maxHealth: the card's max health pool
            initHealth: the card's original max health pool
            #skills: the card's skills
        """
        self._id = id
        self._name = name
        self._cost = cost

        self._damage = damage
        self._initDmg = damage
        
        self._health = health
        self._maxHealth = health
        self._initHealth = health
        #self._skills = skills


    #
    @property
    def id(self):
        return self._id
    #
    @property
    def name(self):
        return self._name
    #
    @property
    def cost(self):
        return self._cost
    #
    @cost.setter
    def cost(self, value):
        self._cost = value
    #
    @property
    def damage(self):
        return self._damage
    #
    @damage.setter
    def damage(self, value):
        self._damage = value
    #
    @property
    def initDmg(self):
        return self._initDmg
    #
    @property
    def health(self):
        return self._health
    #
    @health.setter
    def health(self, value):
        self._health = value
    #
    @property
    def maxHealth(self):
        return self._maxHealth
    #
    @maxHealth.setter
    def maxHealth(self, value):
        self._maxHealth = value
    #
    @property
    def initHealth(self):
        return self._initHealth


    def __str__(self):
        """
        Helper function to visualize the card in the command line
        """
        return f"id:{self.id} N:'{self.name}'\nC:{self.cost} A:{self.damage} H:{self.health}\n"


    def __repr__(self):
        return str(self)
        

    def attack(self, other):
        base_dmg = self.damage
        #check self buffs and debuffs add them to base_dmg
        total_dmg = base_dmg + 0

        base_health = other.health
        #check other buffs and debuffs and modify the dmg dealth to base_health
        remaining_health = base_health - total_dmg*(1)

        #finally subtract dmg dealt from health and apply to card stat
        other.health = remaining_health


if __name__ == "__main__":
    c1 = Card(1, "Squire", 2, 2, 2)
    c2 = Card(2, "Knight", 3, 4, 3)