class VierGewinntBoard:
    def __init__(self):
        #self.name = name
        self.board = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]
        self.last_played_position = [0, 0]

    def file_not_full(self, file):
        if self.board[0][file] != 0:
            return True
        else:
            return False

    def add_chip(self, player, file):
        file_local = file + 1
        board = self.board
        for row in range(len(board)):
            if row == 5: #and board[row][file]==0:
                board[row] = player.name
                self.last_played_position = [row, file]
                break
            elif board[row + 1][file_local] == 0:
                continue
            else:
                board[row][file_local] = player.name
                self.last_played_position = [row, file]
                break

    def check_winner(self, position):
        board = self.board
        x = position[0]
        y = position[1]
        val = board[x][y]

        # check top vertical
        for i in range(4):
            try:
                if board[x - i][y] != val:
                    return False
            except IndexError:
                break
            return True

        # check bottom vertical
        for i in range(4):
            try:
                if board[y - i][x] != val:
                    return False
            except IndexError:
                break
            return True

        # check right horizontal
        for i in range(4):
            try:
                if board[x + i][y] != val:
                    return False
            except IndexError:
                break
            return True

        # check left horizontal
        for i in range(4):
            try:
                if board[y + i][y] != val:
                    return False
            except IndexError:
                break
            return True

        # check top left diagonal
        for i in range(4):
            try:
                if board[x - i][y - i] != val:
                    return False
            except IndexError:
                break
            return True

        # check top right diagonal
        for i in range(4):
            try:
                if board[x - i][y + i] != val:
                    return False
            except IndexError:
                break
            return True

        # check bottom right diagonal
        for i in range(4):
            try:
                if board[x + i][y + i] != val:
                    return False
            except IndexError:
                break
            return True

        # check bottom left diagonal
        for i in range(4):
            try:
                if board[x + i][y - i] != val:
                    return False
            except IndexError:
                break
            return True
