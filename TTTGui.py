from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QApplication, QSizePolicy
from PySide6.QtGui import QFont

from TTTLogic import TicTacToeLogic

class TTTGui(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TicTacToe HENTAI")
        self.logic=TicTacToeLogic()
        self.layout=QGridLayout()
        self.setLayout(self.layout)
        self.button = QPushButton("")
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):

                button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                button.setFont(QFont("Arial", 24))
                button.clicked.connect(lambda checked, r=row, c=col: self.logic.make_move(r, c))
                self.layout.addWidget(button, row, col)
                self.board[row][col] = button

