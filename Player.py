import random
from Card import Card


class Deck:
    def __init__(self):
        """
        A class that represents a Card deck of a Player
            cards: a list containing all the Card objects
            cardCount: the amount of playable cards in the deck
            size: the maximum amount of cards that can be in the deck
        """
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
        """
        A function that allows a card to be put into the deck
        """
        if card is None:
            return 0
        if self._cardCount < self._size:
            self._cards.append(card)
            self._cardCount += 1
    

    def removeCard(self):
        """
        A function that allows a card to be removed from the deck
            returns the Card object that was removed from the deck
        """
        if self._cardCount > 0:
            card = self._cards.pop()
            self._cardCount -= 1
            return card
        return None


    def shuffle(self):
        """
        A function that randomly shuffles the cards in the deck
        """
        random.shuffle(self._cards)


class Hand:
    def __init__(self):
        """
        A class that represents the Card objects in a Player's hand
            cards: a list containing the cards in the player's hand
            cardCount: the number of cards currently in the player's hand
            size: the maximum amount of cards that a player can hold in their hand
        """
        self._cards = []
        self._cardCount = 0
        self._size = 6

    
    @property
    def cardCount(self):
        return self._cardCount

    @property
    def size(self):
        return self._size


    def __str__(self):
        cards = ''
        for i in range(len(self._cards)):
            cards += f"{i+1}{str(self._cards[i])}{i+1}\t"
        return cards


    def addCard(self, card):
        """
        A function that adds a Card to the Player's hand
        """
        if card is None:
            return
        if self._cardCount < self._size:
            self._cards.append(card)
            self._cardCount += 1
    

    def removeCard(self, pos):
        """
        A function that removes a Card at a given position from the player's hand
            returns the removed Card
        """
        if pos < self.cardCount and self._cardCount > 0:
            card = self._cards.pop(pos)
            self._cardCount -= 1
            return card
        return None


class Player:
    def __init__(self, name):
        """
        A class representing a Player in a Game
            name: the name of the player
            deck: the player's deck
            hand: the player's hand
            health: the player's current health
            maxHealth: the player's maximum health pool
        """
        self.name = name
        self.deck = Deck()
        self.hand = Hand()
        self.health = 30
        self.maxHealth = 30
        self.energy = 2
        self.maxEnergy = 2
        self.energyLimit = 10


    def __str__(self):
        return self.name

    
    def drawCard(self):
        """
        A function that lets a player draw a card from their deck into their hand
        """
        card = self.deck.removeCard()
        if card:
            self.hand.addCard(card)

    
    def increaseEnergy(self):
        """
        
        """
        if self.maxEnergy < self.energyLimit:
            self.maxEnergy += 1
        self.energy = self.maxEnergy


if __name__ == "__main__":

    names = ["graverobber", "witch", "gladiator", "fairy", "thief", "assassin", "pirate", 
            "warrior", "swordsman", "deadeye", "guard", "clay golem", "archer", "mercenary", "gatekeeper", 
            "priestess", "merchant", "jailer", "knight", "goblin", "necromancer", "squire", "ogre", 
            "engineer", "soldier", "horseman", "templar", "bishop", "saint", "wizard"]

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