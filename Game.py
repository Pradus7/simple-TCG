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
        return (f"|1\t{self._board[21]}\t1|2\t{self._board[22]}\t2|3\t{self._board[23]}\t3|4\t{self._board[24]}\t4|5\t{self._board[25]}\t5|\n"
                f"|1\t{self._board[11]}\t1|2\t{self._board[12]}\t2|3\t{self._board[13]}\t3|4\t{self._board[14]}\t4|5\t{self._board[15]}\t5|\n")


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
        self.p1 = Player("p1")
        self.p2 = Player("p2")
        self.board = Board()
        self.turn = self.p1

    
    def play(self, player, cardPos, boardPos):
        """
        A function that lets the player play a card from their hand onto the board
        """
        if player is self.p1:
            if boardPos not in [11, 12, 13, 14, 15]:
                print("invalid position")
                return 0

        if player is self.p2:
            if boardPos not in [21, 22, 23, 24, 25]:
                print("invalid position")
                return 0
        
        if cardPos >= player.hand.cardCount:
            print("you do not have that card in your hand")
            return 0

        card = player.hand.removeCard(cardPos)

        if self.board.addCard(card, boardPos) == 0:
            player.hand.addCard(card)
            print("invalid position")
            return 0

    
    def attack(self, player, boardPos):
        """
        A function that allows a card at the given board position to attack its opposing position
        """
        if player is self.p1:
            if boardPos not in [11, 12, 13, 14, 15]:
                print("invalid position")
                return 0

        if player is self.p2:
            if boardPos not in [21, 22, 23, 24, 25]:
                print("invalid position")
                return 0

        opponentPos = boardPos + 10 if boardPos < 20 else boardPos - 10
        selfCard = self.board.getCard(boardPos)
        opponentCard = self.board.getCard(opponentPos)
        if selfCard is None:
            print("you do not have a card there")
            return 0
        if opponentCard:
            selfCard.attack(opponentCard)
            if self.board.getCard(opponentPos).health <= 0:
                self.board.removeCard(opponentPos)
        elif player is self.p1:
            self.p2.health -= selfCard.attack(opponentCard)
        elif player is self.p2:
            self.p1.health -= selfCard.attack(opponentCard)


    def switchTurn(self):
        """
        A function that switches turns
        """
        if self.turn is self.p1:
            self.turn = self.p2
        else:
            self.turn = self.p1


    def takeTurn(self):
        """
        A function that allows a player to take a turn
            In a turn a player can:
            - draw a card
            - play their cards
            - attack with their played cards
        """
        print(f"{self.turn.name}'s turn")
        self.turn.drawCard()
        while True:
            choice = input("what do you want to do?\n1. play card\n2. attack\n3. end turn\n")
            if choice == "1" or choice.lower == "play card" or choice.lower == "play":
                print(self.board)
                print(self.turn.hand)
                cardPos = int(input(f"which card would you like to play?\n"
                                    f"enter a number between 1 and {self.turn.hand.cardCount}\n")) - 1
                boardPos = int(input(f"which location would you like to place your card?\n"
                                     f"enter a number between 1 and 5\n"))
                boardPos = boardPos + 10 if self.turn is self.p1 else boardPos + 20
                if not self.play(self.turn, cardPos, boardPos) == 0:
                    print(self.board)
                    print("ending turn")
                    break
            elif choice == "2" or choice.lower == "attack":
                print(self.board)
                print(self.turn.hand)
                pos = int(input(f"which card would you like to attack with?\n"
                            f"enter a number between 1 and 5\n"))
                pos = pos + 10 if self.turn is self.p1 else pos + 20
                if not self.attack(self.turn, pos) == 0:
                    print(self.board)
                    print("ending turn")
                    break
            else:
                print("skipping turn")
                break
        self.switchTurn()


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
        g.p2.drawCard()
        
    print(g.p1.hand)
    print(g.p2.hand)
    print()

    g.takeTurn()
    print(g.board)
    print(g.p1.hand)
    print(g.p2.hand)

    g.takeTurn()