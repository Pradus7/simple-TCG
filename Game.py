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
    

    @property
    def board(self):
        return self._board


    def addCard(self, card, pos):
        """
        A function that allows a card to be played onto the board
        returns position if card can be placed, otherwise 0
        """
        if not self.board[pos]:
            self.board[pos] = card
            return pos
        return 0

    
    def removeCard(self, pos):
        """
        A function that allows the removal of a card from the game board
        returns removed card if available, otherwise None
        """
        if self.board[pos]:
            card = self.board[pos]
            self.board[pos] = None
            return card
        return None