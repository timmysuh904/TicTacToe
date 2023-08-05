import random
import copy


class mediumbot:
    def __init__(self, player):
        self.player = player

    def select_move(self, board):
        lose = None
        moves = board.get_legal_moves()

        for i in range(len(moves)):
            row = moves[i][0]
            column = moves[i][1]
            copyboard = copy.deepcopy(board)
            copyboard.make_move(row, column, self.player)
            if copyboard.find_winner() == self.player:
                return [row, column]

            losingmoves = copyboard.get_legal_moves()
            for j in range(len(losingmoves)):
                row2 = losingmoves[j][0]
                column2 = losingmoves[j][1]
                copyboard2 = copy.deepcopy(copyboard)
                copyboard2.make_move(row2, column2, "X")
                if copyboard2.find_winner() == "X":
                    lose = [row2, column2]

        if lose is not None:
            return lose

        return random.choice(moves)
