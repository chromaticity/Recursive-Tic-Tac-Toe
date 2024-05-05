# 0 Represents Empty, -1 represents O, and 1 represents X in the game grid
# In addition, 2 represents a board that has been completely filled. For grandboards this means that going down recursively all boards are resolved.


winlines = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)
symboldict = {-1: "O", 1: "X", 0: "·", 2: "No one!"}
cantiewin = False

def gridtoposcalc(depth):
    sidelen = 3**depth
    grid = [()] * (sidelen**2)

    def fillbox(previous, minX, minY, size):
        boxes = []
        for j in range(3):
            for i in range(3):
                boxes.append(((int(minX + i * size / 3)), int((minY + j * size / 3))))
        if size == 3:
            for i in range(9):
                grid[boxes[i][0] + sidelen * boxes[i][1]] = previous + [i]
        else:
            for i in range(9):
                fillbox(previous + [i], boxes[i][0], boxes[i][1], size / 3)

    fillbox([], 0, 0, sidelen)
    return grid


class Piece:  # Represents X or O
    def __init__(self, player):
        self.state = player
        self.depth = 0

    def __str__(self):
        return symboldict[self.state]


# Depth 1 represents a regular game of tic tac toe and every increment represents a level of recursion
class GameBoard:  # Represents A Tic Tac Toe Board
    def __init__(self, depth=1, parent=False, ismovezone=False):
        self.depth = depth
        self.state = 0  # The value of the winner of the game in this board
        self.parent = (
            parent  # Reference to the parent tic tac toe board (if one exists)
        )
        self.ismovezone = ismovezone  # Wether this board is the board that can be moved within on the next turn
        self.isresolved = False

        self.board = []

        if depth == 1:
            for i in range(9):
                self.board.append(Piece(0))
        else:
            for i in range(9):
                self.board.append(GameBoard(depth - 1, self))

    def checkwin(self):  # if boards state is changed then higher boards are checked
        winner = 2

        for i in range(9):
            if self.board[i].state == 0 and (
                self.depth == 1 or not self.board[i].isresolved
            ):
                winner = 0

        for line in winlines:
            if (
                0
                != self.board[line[0]].state
                == self.board[line[1]].state
                == self.board[line[2]].state
                and
                (self.board[line[0]].state != 2 or cantiewin)
            ):
                winner = self.board[line[0]].state
                break

        self.state = winner
        if self.state != 0:
            self.resolve()
            if self.parent != False:
                self.parent.checkwin()

        return winner

    def resolve(self):
        self.isresolved = True
        if self.depth > 1:
            for i in range(9):
                self.board[i].resolve()

    def __str__(self):
        stringified = []
        for pos in self.board:
            stringified.append(str(pos))
        return "".join(stringified)


class TicTacToe:
    def __init__(self, depth=1):
        self.game = GameBoard(depth, False, True)
        self.turn = 1  # Convention is that X goes first
        self.movezone = ()
        self.conversions = gridtoposcalc(depth)
        self.depth = depth

    def move(self, *positions):
        if not (
            positions[0 : len(positions) - (self.game.depth - len(self.movezone))]
            == self.movezone
            or self.movezone == ()
        ):
            return
        deeppos = self.locate(*positions)

        if (
            0 != deeppos.state
            or self.locate(*positions[0 : len(positions) - 1]).isresolved
        ):
            return

        deeppos.state = self.turn
        self.locate(*self.movezone).ismovezone = False
        self.turn *= -1

        if self.depth > 1:
            self.locate(*positions[0 : len(positions) - 1]).checkwin()
            self.movezone = positions[1 : len(positions)]
            while self.locate(*self.movezone).isresolved:
                self.movezone = self.movezone[0 : len(self.movezone) - 1]
                if len(self.movezone) == 0:
                    break
            self.locate(*self.movezone).ismovezone = True
        else:
            self.game.checkwin()
        if self.game.state != 0:
            self.ended()

    def ended(self):
        print("Winner is " + symboldict[self.game.state])

    def printmovezone(self):
        incremented = [x + 1 for x in self.movezone]
        incremented += ["Any"] * (self.depth - len(incremented))
        print(incremented)

    def locate(self, *positions):
        if positions == ():
            return self.game
        deeppos = self.game.board[positions[0]]

        for i in range(1, len(positions)):
            deeppos = deeppos.board[positions[i]]

        return deeppos

    def __str__(self):
        board = str(self.game)
        out = ""

        for i in range(len(board)):
            out += str(self.locate(*self.conversions[i])) + " "
            i += 1
            if i % (3**self.depth) == 0:
                out += "\n"

        return "".join(out)
