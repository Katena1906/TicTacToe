from PySide6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QGridLayout

from TTTLogic import TicTacToeLogic


class TTTGui(QWidget):
    def __init__(self):
        super.__init__()
        self.setWindowTitle("TicTacToe HENTAI")
        self.logic=TicTacToeLogic()
        self.layout=QGridLayout()
        self.setLayout(self.layout)
        self.board = [[None for _ in range(3) for _ in range(3)]]
        self.create_board()


