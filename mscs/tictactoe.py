class Solution:

    # Straightforward: O(m)
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [['#'] * 3 for _ in range(3)]

        def eval(board):
            # horizontal
            if all(cell == board[0][0] and cell != '#' for cell in board[0]):
                return board[0][0]
            if all(cell == board[1][0] and cell != '#' for cell in board[1]):
                return board[1][0]
            if all(cell == board[2][0] and cell != '#' for cell in board[2]):
                return board[2][0]

            # vertical
            if all(board[i][0] == board[0][0] and board[0][0] != '#' for i in range(3)):
                return board[0][0]
            if all(board[i][1] == board[0][1] and board[0][1] != '#' for i in range(3)):
                return board[0][1]
            if all(board[i][2] == board[0][2] and board[0][2] != '#' for i in range(3)):
                return board[0][2]

            # diagnal
            if board[0][0] == board[1][1] == board[2][2] != '#':
                return board[0][0]
            if board[0][2] == board[1][1] == board[2][0] != '#':
                return board[0][2]
            return '#'

        for i, move in enumerate(moves):
            # draw board
            board[move[0]][move[1]] = 'X' if i % 2 == 0 else 'O'

            # eval
            if i >= 4:
                res = eval(board)
                if res == 'X':
                    return 'A'
                if res == 'O':
                    return 'B'
            if i == len(moves) - 1:
                print(i, board)

        return 'Pending' if len(moves) < 9 else 'Draw'
