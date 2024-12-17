from UI.TTT import Ui_TicTacToe

from PySide6.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TicTacToe()
        self.ui.setupUi(self)
        self.buttons =[
            [self.ui.pushButton_12, self.ui.pushButton_11, self.ui.pushButton_10],
            [self.ui.pushButton_18, self.ui.pushButton_16, self.ui.pushButton_15],
            [self.ui.pushButton_17, self.ui.pushButton_14, self.ui.pushButton_13]
        ]


if __name__ == "__main__":

        app = QApplication([])
        window = MainWindow()
        window.show()
        app.exec()