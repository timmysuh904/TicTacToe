import copy
from player import Player

MARKER_TO_CHAR = {
    None: '.',
    Player.x: 'X',
    Player.o: 'O',
}


class Board:
    def __init__(self):
        self.dimension = 3
        self.grid = [[None for y in range(self.dimension)] for x in range(self.dimension)]
        self.moves = []

    def find_winner(self):
        if len(self.moves) < 5:
            return

        #check row for any wins
        for row in range(self.dimension):
            row = set(self.grid[row])
            if len(row) == 1:
                value = row.pop()
                if value is not None:
                    return value

        #check column for any wins
        for i in range(self.dimension):
            column = set()
            for j in range(self.dimension):
                column.add(self.grid[j][i])
            if len(column) == 1:
                value = column.pop()
                if value is not None:
                    return value

        #check diagonals
        diagonal1 = set()
        diagonal1.add(self.grid[0][0])
        diagonal1.add(self.grid[1][1])
        diagonal1.add(self.grid[2][2])

        if len(diagonal1) == 1:
            value = diagonal1.pop()
            if value is not None:
                return value

        diagonal2 = set()
        diagonal2.add(self.grid[0][2])
        diagonal2.add(self.grid[1][1])
        diagonal2.add(self.grid[2][0])

        if len(diagonal2) == 1:
            value = diagonal2.pop()
            if value is not None:
                return value

        #no winner
        return None

    def is_space_empty(self, row, col):
        return self.grid[row][col] is None

    def make_move(self, row, col, player):
        if self.is_space_empty(row, col):
            self.grid[row][col] = player
            self.moves.append([row, col])
        else:
            raise Exception("Space is already occupied!")

    def last_move(self):
        return self.moves[-1]

    def get_legal_moves(self):
        moves = []
        for i in range(self.dimension):
            for j in range(self.dimension):
                if self.is_space_empty(i, j):
                    moves.append([i, j])
        return moves

    def __deepcopy__(self, memodict={}):
        dp = Board()
        dp.grid = copy.deepcopy(self.grid)
        dp.moves = copy.deepcopy(self.moves)
        return dp
