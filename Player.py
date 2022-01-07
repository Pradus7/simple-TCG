import random
from Card import Card

class Deck:
    def __init__(self):
        self._cards = []
        self._cardCount = 0
        self._size = 30


    def __str__(self):
        cards = sorted(self._cards, key=lambda card: card.cost)
        return '\n\n'.join([str(card) for card in cards])
    

    def __repr__(self):
        return str(self)
    

    def addCard(self, card):
        if self._cardCount < self._size:
            self._cards.append(card)
            self._cardCount += 1
    

    def removeCard(self):
        if self._cardCount > 0:
            card = self._cards.pop
            self._cardCount -= 1
        return card


    def shuffle(self):
        random.shuffle(self._cards)


class Hand:
    def __init__(self):
        self._cards = []
        self._cardCount = 0
        self._size = 8


    def addCard(self, card):
        if self._cardCount < self._size:
            self._cards.append(card)
            self._cardCount += 1
    
    
    def removeCard(self):
        if self._cardCount > 0:
            card = self._cards.pop
            self._cardCount -= 1
        return card


class Player:
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()
        self.health = 30
        self.maxHealth = 30


if __name__ == "__main__":
    names = ["graverobber", "witch", "slave driver", "mechanical golem", "alleyway thief", "assassin", "pirate", 
            "warrior", "swordsman", "deadeye", "town guard", "clay golem", "tower mage", "mercenary", "gatekeeper", 
            "priestess", "merchant", "jailer", "knight", "fortune teller", "necromancer", "squire", "plague doctor", 
            "steampunk engineer", "soldier", "informant", "templar", "bishop", "holy knight", "wizard"]
    random.shuffle(names)
    cards = []
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
        cards.append(Card(i, names[i].title(), cost, dmg, health))

    deck1 = Deck()
    deck2 = Deck()
    for card in cards:
        deck1.addCard(card)
        deck2.addCard(card)

    print(deck1)