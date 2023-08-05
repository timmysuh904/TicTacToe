import random
import copy


class easybot:
    def __init__(self, player):
        self.player = player

    def select_move(self, board):
        moves = board.get_legal_moves()
        for i in range(len(moves)):
            row = moves[i][0]
            column = moves[i][1]
            copyboard = copy.deepcopy(board)
            copyboard.make_move(row, column, self.player)
            if copyboard.find_winner() == self.player:
                return [row, column]

        return random.choice(moves)
