import copy


class Choice:
    def __init__(self, move, value, depth):
        self.move = move
        self.value = value
        self.depth = depth

    def __str__(self):
        return str(self.move) + ": " + str(self.value)


class hardbot:
    def __init__(self, player):
        self.player = player

    def minimax(self, board, is_max, player, depth):
        winner = board.find_winner()
        if winner == "O":
            return Choice(board.last_move(), 10 - depth, depth)
        elif winner == "X":
            return Choice(board.last_move(), -10 + depth, depth)
        elif len(board.moves) == 9:  # Board is full, it's a tie.
            return Choice(board.last_move(), 0, depth)

        choices = []
        moves = board.get_legal_moves()
        for i in range(len(moves)):
            row, column = moves[i]
            newboard = copy.deepcopy(board)
            newboard.make_move(row, column, player)
            result = self.minimax(newboard, not is_max, "O" if player == "X" else "X", depth + 1)
            result.move = newboard.last_move()
            choices.append(result)

        best_choice = max(choices, key=lambda choice: choice.value) if is_max else min(choices,
                                                                                       key=lambda choice: choice.value)
        return best_choice

    def select_move(self, board):
        choice = self.minimax(board, True, "O", 0)
        return choice.move
