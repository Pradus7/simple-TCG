from Player import Player


class Board:
    def __init__(self):
        """
        A Board class to facilitate a game between 2 Players using Cards
            The board provides 5 slots for each player to place down cards, 
            giving a total of 10 slots to place down cards
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
        return (f"P2 Side\n|1\t{self._board[21]}\t1|2\t{self._board[22]}\t2|3\t{self._board[23]}\t3"
                f"|4\t{self._board[24]}\t4|5\t{self._board[25]}\t5|\n"
                f"|1\t{self._board[11]}\t1|2\t{self._board[12]}\t2|3\t{self._board[13]}\t3"
                f"|4\t{self._board[14]}\t4|5\t{self._board[15]}\t5|\nP1 Side")


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
        This class allows 2 players to play a TCG by placing down cards and attacking
        opposing cards or the opposing player. The first player to take down the opposing
        player's health down to 0 wins.
            p1: the first player
            p2: the second player
            board: the game board to place down cards
            turn: the current player taking their turn
        """
        self.p1 = Player("p1")
        self.p2 = Player("p2")
        self.board = Board()
        self.turn = self.p1

    
    def play(self, player, cardPos, boardPos):
        """
        A function that lets the player play a card from their hand onto the board
        """
        if player is self.p1 and boardPos not in [11, 12, 13, 14, 15]:
            print("\ninvalid position\n")
            return 0

        elif player is self.p2 and boardPos not in [21, 22, 23, 24, 25]:
            print("\ninvalid position\n")
            return 0
        
        if cardPos >= player.hand.cardCount:
            print("\nyou do not have that card in your hand\n")
            return 0

        card = player.hand.removeCard(cardPos)

        if card.cost > player.energy:
            player.hand.addCard(card)
            print("\ninsufficient energy\n")
            return 0

        player.energy -= card.cost

        if self.board.addCard(card, boardPos) == 0:
            player.hand.addCard(card)
            print("\ninvalid position\n")
            return 0

    
    def attack(self, player, boardPos):
        """
        A function that allows a card at the given board position to attack its opposing position
        """
        if player is self.p1 and boardPos not in [11, 12, 13, 14, 15]:
            print("\ninvalid position\n")
            return 0

        elif player is self.p2 and boardPos not in [21, 22, 23, 24, 25]:
            print("\ninvalid position\n")
            return 0
        
        selfCard = self.board.getCard(boardPos)

        if selfCard.attacked:
            print("\nthis card already attacked this turn\n")
            return 0
        
        if selfCard is None:
            print("\nyou do not have a card at that position to attack with\n")
            return 0

        opponentPos = boardPos + 10 if boardPos < 20 else boardPos - 10
        opponentCard = self.board.getCard(opponentPos)

        if opponentCard:
            selfCard.attack(opponentCard)
            selfCard.attacked = True

            if self.board.getCard(opponentPos).health <= 0:
                self.board.removeCard(opponentPos)

        elif player is self.p1:
            self.p2.health -= selfCard.attack(opponentCard)
            selfCard.attacked = True

        elif player is self.p2:
            self.p1.health -= selfCard.attack(opponentCard)
            selfCard.attacked = True


    def opponent(self):
        """
        """
        return self.p2 if self.turn is self.p1 else self.p1


    def switchTurn(self):
        """
        A function that switches turns between p1 and p2
        """
        self.turn = self.opponent()

    
    def printTurnInfo(self):
        """
        """
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print(f"P2 Health:{self.p2.health}")
        print(self.board)
        print(f"P1 Health:{self.p1.health}\n\n")
        print(f"Player {self.turn.name}'s turn\n\n")
        print(f"Hand:\n{self.turn.hand}\n")
        print(f"Energy: {self.turn.energy}/{self.turn.maxEnergy}\n\n")


    def takeTurn(self):
        """
        A function that allows a player to take a turn
            In a turn a player can:
            - draw a card
            - play their cards
            - attack with their played cards
        """
        self.turn.drawCard()
        self.turn.increaseEnergy()

        for pos in self.board._board:
            if self.board.getCard(pos) is not None:
                self.board.getCard(pos).attacked = False

        while True:
            self.printTurnInfo()
            choice = input(f"what do you want to do?\n1. play card\n2. attack\n3. end turn\n"
                           f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

            if choice == "1" or choice.lower == "play card" or choice.lower == "play":
                self.printTurnInfo()
                cardPos = int(input(f"\nwhich card would you like to play?\n"
                                    f"enter a number between 1 and {self.turn.hand.cardCount}\n"
                                    f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")) - 1
                self.printTurnInfo()
                boardPos = int(input(f"\nwhich location would you like to place your card?\n"
                                     f"enter a number between 1 and 5\n"
                                     f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"))
                self.printTurnInfo()
                boardPos = boardPos + 10 if self.turn is self.p1 else boardPos + 20

                if not self.play(self.turn, cardPos, boardPos) == 0:
                    continue

            elif choice == "2" or choice.lower == "attack":
                self.printTurnInfo()
                pos = int(input(f"\nwhich card would you like to attack with?\n"
                                f"enter a number between 1 and 5\n"
                                f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"))
                self.printTurnInfo()
                pos = pos + 10 if self.turn is self.p1 else pos + 20

                if not self.attack(self.turn, pos) == 0:
                    if self.opponent().health <= 0:
                        self.printTurnInfo()
                        print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                              f"Player {self.turn} won!"
                              f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        return 1

            else:
                print("ending turn\n\n\n")
                break
            
        self.switchTurn()

    
    def playGame(self):
        """
        """
        from Card import Card
        import random
        print("Game starting\n\n\n\n\n")
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
            self.p1.deck.addCard(Card(i, names[i].title(), cost, dmg, health))
            self.p2.deck.addCard(Card(i, names[i].title(), cost, dmg, health))
        #end of card generation

        self.p1.deck.shuffle()
        self.p2.deck.shuffle()

        for i in range(self.p1.hand.size-3):
            self.p1.drawCard()
            self.p2.drawCard()

        while True:
            if self.takeTurn() == 1:
                break


if __name__ == "__main__":
    g = Game()
    g.playGame()