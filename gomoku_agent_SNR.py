# Gomoku AI Agent
# Authors: Nandini Rampal and Roopireddy Snisha Reddy


import random

class GomokuAgent:

    def __init__(self, agent_symbol, blank_symbol, opponent_symbol):
        self.me = agent_symbol
        self.blank = blank_symbol
        self.opp = opponent_symbol

    def play(self, board):
        empty_cells = self.get_empty_cells(board)

        for cell in empty_cells:
            if self.makes_five(board, cell, self.me):
                return cell

        for cell in empty_cells:
            if self.makes_five(board, cell, self.opp):
                return cell

        for cell in empty_cells:
            row, col = cell

            for d_row, d_col in [(0, 1), (1, 0), (1, 1), (1, -1)]:
                r = row - d_row
                c = col - d_col 

                if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == self.me:
                    return cell

        return random.choice(empty_cells)

    def get_empty_cells(self, board):
        cells = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == self.blank:
                    cells.append((row, col))
        return cells

    def makes_five(self, board, cell, symbol):
        """If `symbol` were placed at `cell`, would that make 5 in a row?"""
        row, col = cell
        board[row][col] = symbol  # try the move

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        found_five = False
        for d_row, d_col in directions:
            count = 1
            r, c = row + d_row, col + d_col
            while 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == symbol:
                count += 1
                r += d_row
                c += d_col
            r, c = row - d_row, col - d_col
            while 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == symbol:
                count += 1
                r -= d_row
                c -= d_col
            if count >= 5:
                found_five = True

        board[row][col] = self.blank  # undo the move
        return found_five
