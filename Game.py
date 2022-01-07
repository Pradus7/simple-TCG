from Player import Player


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
        return f"|\t{self._board[21]}\t|\t{self._board[22]}\t|\t{self._board[23]}\t|\t{self._board[24]}\t|\t{self._board[25]}\t|\n|\t{self._board[11]}\t|\t{self._board[12]}\t|\t{self._board[13]}\t|\t{self._board[14]}\t|\t{self._board[15]}\t|"


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


    def getCard(self, pos):
        return self._board[pos]
    

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
        
        if cardPos >= player.hand.cardCount:
            print("you do not have that card in your hand")
            return

        card = player.hand.removeCard(cardPos)
        if self.board.addCard(card, boardPos) == 0:
            print("invalid position")

    
    def attack(self, player, boardPos):
        """
        A function that allows a card at the given board position to attack its opposing position
        """
        if player is self.p1:
            if boardPos not in [11, 12, 13, 14, 15]:
                print("invalid position")
                return

        if player is self.p2:
            if boardPos not in [21, 22, 23, 24, 25]:
                print("invalid position")
                return

        opponentPos = boardPos + 10 if boardPos < 20 else boardPos - 10
        selfCard = self.board.getCard(boardPos)
        opponentCard = self.board.getCard(opponentPos)
        if opponentCard:
            selfCard.attack(opponentCard)
            if self.board.getCard(opponentPos).health <= 0:
                self.board.removeCard(opponentPos)
        elif player is self.p1:
            self.p2.health -= selfCard.attack(opponentCard)
        elif player is self.p2:
            self.p1.health -= selfCard.attack(opponentCard)


if __name__ == "__main__":

    from Card import Card
    import random

    g = Game()

    names = ["graverobber", "witch", "gladiator", "fairy", "thief", "assassin", "pirate", 
            "warrior", "swordsman", "deadeye", "guard", "clay golem", "archer", "mercenary", "gatekeeper", 
            "priestess", "merchant", "jailer", "knight", "goblin", "necromancer", "squire", "ogre", 
            "engineer", "soldier", "horseman", "templar", "bishop", "saint", "wizard"]

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
        print(g.p1.deck.cardCount)
    for i in range(3):
        g.p2.drawCard()
        print(g.p2.deck.cardCount)

    print(g.p1.hand)
    print()
    print(g.p1.hand.cardCount)
    print(g.p2.hand.cardCount)
    print()

    g.play(g.p1, 2, 11) #valid
    g.play(g.p1, 0, 21) #invalid since it's not the player's side of the board
    g.play(g.p1, 8, 13) #invalid since the player does not have an 8th card in their hand
    g.play(g.p1, 3, 13) #valid
    g.play(g.p1, 1, 11) #invalid card already exists at that position
    g.play(g.p1, 1, 12) #valid
    g.play(g.p1, 1, 14) #valid
    g.play(g.p1, 1, 15) #valid

    g.play(g.p2, 2, 11) #invalid side
    g.play(g.p2, 1, 23) #valid
    g.play(g.p2, 1, 21) #valid
    g.play(g.p2, 0, 22) #valid
    g.play(g.p2, 0, 24) #invalid, hand ran out of cards

    print(g.p1.hand.cardCount)
    print(g.p2.hand.cardCount)
    print()

    print(g.board)
    print()
    print(g.p1.hand)
    print()
    print(g.p2.hand)

    g.attack(g.p1, 13)

    print()
    print(g.board)

    for i in range(3):
        g.p2.drawCard()
        print(g.p2.deck.cardCount)

    g.play(g.p2, 0, 23) #valid
    g.play(g.p2, 0, 24) #valid
    #g.play(g.p2, 0, 25) #valid

    print()
    print(g.board)

    g.attack(g.p1, 11)
    g.attack(g.p1, 12)
    g.attack(g.p1, 13)
    g.attack(g.p1, 14)
    g.attack(g.p1, 15)

    print()
    print(g.board)

    print(g.p1.health)
    print(g.p2.health)