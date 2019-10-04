# version 1.0
def make_board(s):
    board = np.empty((9,9),dtype="int8")
    for r in range(9):
        for c in range(9):
            while not ('0' <= s[0] <= '9'):
                s = s[1:]
            board[r,c] = s[0]
            s = s[1:]

    return board
