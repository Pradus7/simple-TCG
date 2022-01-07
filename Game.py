from player import Player


class Board:
    def __init__(self):
        """
        A Board class to facilitate a game between 2 Players using Cards
            The board provides 5 slots for each player to place down cards, giving a total of 12 slots
            A visual representation of the game board:
                  P2
            21 22 23 24 25
            11 12 13 14 15
                  P1
        """
        self._board = {
            21: None, 22: None, 23: None, 24: None, 25: None, 
            11: None, 12: None, 13: None, 14: None, 15: None
        }

    
    def __str__(self):
        return f"|{self._board[21]}|{self._board[22]}|{self._board[23]}|{self._board[24]}|{self._board[25]}|\n|{self._board[11]}|{self._board[12]}|{self._board[13]}|{self._board[14]}|{self._board[15]}|"


    def __repr__(self):
        return str(self)


    def addCard(self, card, pos):
        """
        A function that allows a card to be played onto the board
        returns position if card can be placed, otherwise 0
        """
        if not self._board[pos]:
            self._board[pos] = card
            return pos
        return 0

    
    def removeCard(self, pos):
        """
        A function that allows the removal of a card from the game board
        returns removed card if available, otherwise None
        """
        if self._board[pos]:
            card = self._board[pos]
            self._board[pos] = None
            return card
        return None


class Game:
    def __init__(self):
        """
        The Game class allows 2 players to play a game on a Board by placing Cards on the board and damaging each other
        """
        self.p1 = Player()
        self.p2 = Player()
        self.board = Board()

    
    def play(self, player, cardPos, boardPos):
        """
        A function that lets the player play a card from their hand onto the board
        """
        if player is self.p1:
            if boardPos not in [11, 12, 13, 14, 15]:
                print("invalid position")
                return

        if player is self.p2:
            if boardPos not in [21, 22, 23, 24, 25]:
                print("invalid position")
                return
        
        if cardPos > player.hand.cardCount:
            print("you do not have that card in your hand")
            return

        card = player.hand.removeCard(cardPos)
        self.board.addCard(card, boardPos)


if __name__ == "__main__":
    from card import Card
    import random

    g = Game()

    names = ["graverobber", "witch", "slave driver", "mechanical golem", "alleyway thief", "assassin", "pirate", 
            "warrior", "swordsman", "deadeye", "town guard", "clay golem", "tower mage", "mercenary", "gatekeeper", 
            "priestess", "merchant", "jailer", "knight", "fortune teller", "necromancer", "squire", "plague doctor", 
            "steampunk engineer", "soldier", "informant", "templar", "bishop", "holy knight", "wizard"]

    random.shuffle(names)

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
        g.p1.deck.addCard(Card(i, names[i].title(), cost, dmg, health))
        g.p2.deck.addCard(Card(i, names[i].title(), cost, dmg, health))
    
    
    print(g.p1.deck)
    print()
    print(g.board)
    print()

    
    g.p1.deck.shuffle()
    g.p2.deck.shuffle()

    
    for i in range(10):
        g.p1.drawCard()
    for i in range(6):
        g.p2.drawCard()


    print(g.p1.hand)
    print()

    g.play(g.p1, 2, 11)

    g.play(g.p1, 0, 21)

    g.play(g.p1, 8, 13)

    g.play(g.p2, 2, 11)

    g.play(g.p2, 1, 23)

    g.play(g.p1, 3, 13)

    print(g.board)
    print()
    print(g.p1.hand)
    print()
    print(g.p2.hand)


    