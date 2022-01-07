import random
from Card import Card


class Deck:
    def __init__(self):
        self._cards = []
        self._cardCount = 0
        self._size = 30


    @property
    def cardCount(self):
        return self._cardCount


    def __str__(self):
        cards = sorted(self._cards, key=lambda card: card.cost)
        return ''.join([str(card) for card in cards])
    

    def __repr__(self):
        return str(self)
    

    def addCard(self, card):
        if self._cardCount < self._size:
            self._cards.append(card)
            self._cardCount += 1
    

    def removeCard(self):
        if self._cardCount > 0:
            card = self._cards.pop()
            self._cardCount -= 1
            return card
        return None


    def shuffle(self):
        random.shuffle(self._cards)


class Hand:
    def __init__(self):
        self._cards = []
        self._cardCount = 0
        self._size = 8

    
    @property
    def cardCount(self):
        return self._cardCount


    def __str__(self):
        return str(self._cards)


    def addCard(self, card):
        if not card:
            return
        if self._cardCount < self._size:
            self._cards.append(card)
            self._cardCount += 1
    

    def removeCard(self, pos):
        if pos < self.cardCount and self._cardCount > 0:
            card = self._cards.pop(pos)
            self._cardCount -= 1
            return card
        return None


class Player:
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
        self.health = 30
        self.maxHealth = 30

    
    def drawCard(self):
        """
        A function that lets a player draw a card from their deck into their hand
        """
        card = self.deck.removeCard()
        if card:
            self.hand.addCard(card)


if __name__ == "__main__":

    names = ["graverobber", "witch", "gladiator", "mechanical golem", "alleyway thief", "assassin", "pirate", 
            "warrior", "swordsman", "deadeye", "town guard", "clay golem", "tower mage", "mercenary", "gatekeeper", 
            "priestess", "merchant", "jailer", "knight", "fortune teller", "necromancer", "squire", "plague doctor", 
            "steampunk engineer", "soldier", "informant", "templar", "bishop", "holy knight", "wizard"]

    random.shuffle(names)

    deck1 = Deck()
    deck2 = Deck()

    costList = [1]*4 + [2]*6 + [3]*8 + [4]*9 + [5]*7 + [6]*5 + [7]*3 + [8]*2 + [9]*1

    for i in range(30):

        cost = random.choice(costList)
        dmg = max(1,random.randint(cost-2,cost+2))
        health = max(1,random.randint(cost-2,cost+2))

        if (dmg+health) > cost*2:
            if dmg > cost:
                health -= 2
            elif health > cost:
                dmg -= 2

        elif (dmg+health) < cost*2:
            if dmg < cost:
                health += 2
            elif health < cost:
                dmg += 2

        dmg = max(1, dmg)
        health = max(1, health)
        deck1.addCard(Card(i, names[i].title(), cost, dmg, health))
        deck2.addCard(Card(i, names[i].title(), cost, dmg, health))

    print(deck1)