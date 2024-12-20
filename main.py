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
        self.ui.pushButton_2.clicked.connect(self.close)

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].clicked.connect(lambda checked, row=i, col=j: self.on_button_clicked(row, col))


    def close(self):
        super().close()

    def click_reset(self):
        self.logic.reset_game()
        self.enable_buttons()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText("")
        self.ui.label_2.setText(f"Current: X")
        self.ui.label_3.setText(f"Winner: ")


    def on_button_clicked(self, row, col):
        if self.logic.make_move(row, col):
            self.buttons[row][col].setText(self.logic.c_player)
            self.logic.switch_player()
            self.ui.label_2.setText(f"Current: {self.logic.c_player}")

        if  self.logic.check_winner():
            self.disable_buttons()
            if self.logic.c_player=="X":
              self.ui.label_3.setText("Winner: O")
            else:
                self.ui.label_3.setText("Winner: X")
        if self.logic.check_draw():
            self.disable_buttons()
            self.ui.label_3.setText("Winner: None")



    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

    def enable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(True)

if __name__ == "__main__":
        app = QApplication()
        window = MainWindow()
        window.show()
        app.exec()