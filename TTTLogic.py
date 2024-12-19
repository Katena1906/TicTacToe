
class TicTacToeLogic:
    def __init__(self):
        self.board= [["" for _ in range(3)] for _ in range(3)]
        self.c_player="X"

    def make_move(self, rows, cols):
        if self.board[rows][cols] == "":
            self.board[rows][cols] = self.c_player
            return True
        return False

    def check_winner(self):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]!="":
                return self.board[i][0]
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]!="":
                return self.board[0][i]

        if self.board[0][0]==self.board[1][1]==self.board[2][2]!="":
            return self.board[0][0]
        if self.board[0][2]==self.board[1][1]==self.board[2][0]!="":
            return self.board[0][2]
        return None

    def check_draw(self):
        if self.check_winner() is not None:
            return False

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False

        return True

    def switch_player(self):
        if self.c_player=="X":
            self.c_player="O"
        else:
            self.c_player="X"

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.c_player = "X"


