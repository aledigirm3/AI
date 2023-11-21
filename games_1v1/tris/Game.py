import numpy as np


class Game:
    def __init__(self):
        self.initializeGame()

    def initializeGame(self):
        self.currentState = [['.', '.', '.'],
                             ['.', '.', '.'],
                             ['.', '.', '.']]
        # player who do first move
        self.playerTurn = 'X'

    def drawBoard(self):
        print()
        for i in range(len(self.currentState)):
            for j in range(len(self.currentState[i])):
                print(self.currentState[i][j] + '|', end='')
            print()

        print()

        # is the move valid?
    def isValid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.currentState[px][py] != '.':
            return False
        return True

    # tris done! check
    def isEnd(self):
        # on raw
        for i in range(len(self.currentState)):
            if self.currentState[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.currentState[i] == ['O', 'O', 'O']:
                return 'O'

        # on column
        for i in range(len(self.currentState)):
            if self.currentState[0][i] == self.currentState[1][i] == self.currentState[2][i] and self.currentState[0][i] != ['']:
                return self.currentState[0][i]

        # on diagonals
        if self.currentState[0][0] == self.currentState[1][1] == self.currentState[2][2] and self.currentState[0][0] != ['.']:
            return self.currentState[0][0]

        if self.currentState[0][2] == self.currentState[1][1] == self.currentState[2][0] and self.currentState[0][2] != ['.']:
            return self.currentState[0][2]

        # still not (maybe tie)
        for i in range(len(self.currentState)):
            for j in range(len(self.currentState)):
                if self.currentState[i][j] == '.':
                    return False
        return 'tie'

    # player 'O' is max -> in this use case is the AI
    def max(self):
        # -1 -> lost
        # 0 -> tie
        # 1 -> won
        maxv = -np.inf
        px = None
        py = None

        result = self.isEnd()
        if result == 'O':
            return (1, 0, 0)
        if result == 'X':
            return (-1, 0, 0)
        if result == 'tie':
            return (0, 0, 0)

        for i in range(len(self.currentState)):
            for j in range(len(self.currentState)):
                if self.currentState[i][j] == '.':
                    self.currentState[i][j] = 'O'
                    (minv, min_px, min_py) = self.min()

                    if minv > maxv:
                        maxv = minv
                        px = i
                        py = j
                    self.currentState[i][j] = '.'

        return (maxv, px, py)

    # player 'X' is min -> physical player
    def min(self):
        # -1 -> won
        # 0 -> tie
        # 1 -> lost
        minv = np.inf
        px = None
        py = None

        result = self.isEnd()
        if result == 'O':
            return (1, 0, 0)
        if result == 'X':
            return (-1, 0, 0)
        if result == 'tie':
            return (0, 0, 0)

        for i in range(len(self.currentState)):
            for j in range(len(self.currentState)):
                if self.currentState[i][j] == '.':
                    self.currentState[i][j] = 'X'
                    (maxv, max_px, max_py) = self.max()

                    if minv > maxv:
                        minv = maxv
                        px = i
                        py = j

                    self.currentState[i][j] = '.'

        return (minv, px, py)

    def play(self):
        while True:
            self.drawBoard()
            result = self.isEnd()
            if result == 'O':
                print("Player 'O' won!")
                return
            if result == 'X':
                print("Player 'X' won!")
                return
            if result == 'tie':
                print('Tie... Play again to find the best!')
                return

            while True:
                print(
                    '==================================================================================')
                if self.playerTurn == 'X':
                    (minv, min_px, min_py) = self.min()
                    print("TURN : X\n")
                    print('Recommended move: row -> ' +
                          str(min_px) + ', column -> ' + str(min_py))
                    px = int(input('Choose row number: '))
                    py = int(input('Choose column number: '))
                    if self.isValid(px, py):
                        self.currentState[px][py] = 'X'
                        self.playerTurn = 'O'
                        break
                    print('Forbidden move! RETRY')

                if self.playerTurn == 'O':
                    print("TURN : O\n")
                    (maxv, max_px, max_py) = self.max()
                    self.currentState[max_px][max_py] = 'O'
                    self.playerTurn = 'X'
                    break
                print(
                    '==================================================================================')
