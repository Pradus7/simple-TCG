class Board:
    def __init__(self):
        """
        A Board class to facilitate a game between 2 Players using Cards
            The board provides 5 slots for each player to place down cards, giving a total of 12 slots
        """
        self._side1 = []
        self._side2 = []
        self._side1Cards = 0
        self._side2Cards = 0
        self._maxCards = 5