



from gomoku_agent_SNR import GomokuAgent as MyAgent
from dumb_agent import GomokuAgent as DumbAgent

SIZE = 15
BLANK = '.'
AGENT1 = 'X'
AGENT2 = 'O'
HISTORY_FILE = 'gomoku_history.txt'


def print_board(board, move_numbers):
  
    for r, row in enumerate(board):
        cells = []
        for c, symbol in enumerate(row):
            if symbol == BLANK:
                cells.append('  .  ')
            else:
                label = f'{symbol}{move_numbers[r][c]}'
                cells.append(label.center(5))
        print(''.join(cells))
    print()


def check_five(board, row, col, symbol):

    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for d_row, d_col in directions:
        count = 1
        r, c = row + d_row, col + d_col
        while 0 <= r < SIZE and 0 <= c < SIZE and board[r][c] == symbol:
            count += 1
            r += d_row
            c += d_col
        r, c = row - d_row, col - d_col
        while 0 <= r < SIZE and 0 <= c < SIZE and board[r][c] == symbol:
            count += 1
            r -= d_row
            c -= d_col
        if count >= 5:
            return True
    return False



def main():
    board = [[BLANK] * SIZE for _ in range(SIZE)]
    move_numbers = [[None] * SIZE for _ in range(SIZE)]  # which move number placed each stone
    move_count = 0
    agent1 = MyAgent(agent_symbol=AGENT1, blank_symbol=BLANK, opponent_symbol=AGENT2)
    agent2 = DumbAgent(agent_symbol=AGENT2, blank_symbol=BLANK, opponent_symbol=AGENT1)


    while True:
        row, col = agent1.play(board)
        board[row][col] = AGENT1
        move_count += 1
        move_numbers[row][col] = move_count
        print(f"AGENT1 plays {row},{col}")
       # print_board(board, move_numbers)
        
        if check_five(board, row, col, AGENT1):
            print("AGENT1 wins!")
        
            break

        row, col = agent2.play(board)
        board[row][col] = AGENT2
        move_count += 1
        move_numbers[row][col] = move_count
        print(f"Agent2 plays {row},{col}")
       # print_board(board, move_numbers)
 
        if check_five(board, row, col, AGENT2):
            print("Agent2 wins!")
    
            break
    print_board(board, move_numbers)


if __name__ == "__main__":
    main()
