from UI.TTT import Ui_TicTacToe
from TTTLogic import TicTacToeLogic

from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.logic=TicTacToeLogic()
        self.ui = Ui_TicTacToe()
        self.ui.setupUi(self)
        self.buttons = [
            [self.ui.pushButton_12, self.ui.pushButton_11, self.ui.pushButton_10],
            [self.ui.pushButton_18, self.ui.pushButton_16, self.ui.pushButton_15],
            [self.ui.pushButton_17, self.ui.pushButton_14, self.ui.pushButton_13]
        ]
        self.ui.pushButton.clicked.connect(self.click_reset)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(lambda checked, row=i, col=j: self.on_button_clicked(row, col))
    def click_reset(self):
        self.logic.reset_game()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText("")

    def on_button_clicked(self, row, col):
        if self.logic.make_move(row, col):
            self.buttons[row][col].setText(self.logic.c_player)
            self.logic.switch_player()
            #self.logic.check_winner()
            #self.logic.check_draw()


if __name__ == "__main__":

        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec()