# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TTT.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_TicTacToe(object):
    def setupUi(self, TicTacToe):
        if not TicTacToe.objectName():
            TicTacToe.setObjectName(u"TicTacToe")
        TicTacToe.resize(788, 782)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TicTacToe.sizePolicy().hasHeightForWidth())
        TicTacToe.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Yu Gothic"])
        font.setPointSize(26)
        TicTacToe.setFont(font)
        TicTacToe.setIconSize(QSize(24, 24))
        self.centralwidget = QWidget(TicTacToe)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_14 = QPushButton(self.centralwidget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy)
        self.pushButton_14.setMinimumSize(QSize(120, 120))
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 255, 179))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 0, 127, 228))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        brush2 = QBrush(QColor(249, 249, 249, 77))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        brush3 = QBrush(QColor(0, 0, 0, 92))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.pushButton_14.setPalette(palette)
        self.pushButton_14.setStyleSheet(u"font: 36pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_14, 2, 1, 1, 1)

        self.pushButton_17 = QPushButton(self.centralwidget)
        self.pushButton_17.setObjectName(u"pushButton_17")
        sizePolicy.setHeightForWidth(self.pushButton_17.sizePolicy().hasHeightForWidth())
        self.pushButton_17.setSizePolicy(sizePolicy)
        self.pushButton_17.setMinimumSize(QSize(120, 120))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.pushButton_17.setPalette(palette1)
        self.pushButton_17.setStyleSheet(u"font: 36pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_17, 2, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.centralwidget)
        self.pushButton_18.setObjectName(u"pushButton_18")
        sizePolicy.setHeightForWidth(self.pushButton_18.sizePolicy().hasHeightForWidth())
        self.pushButton_18.setSizePolicy(sizePolicy)
        self.pushButton_18.setMinimumSize(QSize(120, 120))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.pushButton_18.setPalette(palette2)
        self.pushButton_18.setStyleSheet(u"font: 36pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_18, 1, 0, 1, 1)

        self.pushButton_15 = QPushButton(self.centralwidget)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        self.pushButton_15.setMinimumSize(QSize(120, 120))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.pushButton_15.setPalette(palette3)
        self.pushButton_15.setStyleSheet(u"font: 36pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_15, 1, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.centralwidget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        sizePolicy.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy)
        self.pushButton_11.setMinimumSize(QSize(120, 120))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.pushButton_11.setPalette(palette4)
        self.pushButton_11.setStyleSheet(u"font: 36pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_11, 0, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.centralwidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        sizePolicy.setHeightForWidth(self.pushButton_16.sizePolicy().hasHeightForWidth())
        self.pushButton_16.setSizePolicy(sizePolicy)
        self.pushButton_16.setMinimumSize(QSize(120, 120))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.pushButton_16.setPalette(palette5)
        self.pushButton_16.setStyleSheet(u"font: 36pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_16, 1, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.centralwidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy)
        self.pushButton_12.setMinimumSize(QSize(120, 120))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.pushButton_12.setPalette(palette6)
        self.pushButton_12.setStyleSheet(u"font: 36pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_12, 0, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.centralwidget)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy)
        self.pushButton_10.setMinimumSize(QSize(120, 120))
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.pushButton_10.setPalette(palette7)
        self.pushButton_10.setStyleSheet(u"font: 36pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_10, 0, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.centralwidget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        self.pushButton_13.setMinimumSize(QSize(120, 120))
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        self.pushButton_13.setPalette(palette8)
        self.pushButton_13.setStyleSheet(u"font: 36pt \"Arial\";")

        self.gridLayout.addWidget(self.pushButton_13, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"font: 48pt \"Vladimir Script\";")
        self.label.setTextFormat(Qt.TextFormat.AutoText)

        self.verticalLayout.addWidget(self.label)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u"D:/User/5409375404118108405.jpg"))

        self.verticalLayout.addWidget(self.label_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"font: 48pt \"Vladimir Script\";")

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"font: 48pt \"Vladimir Script\";")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 48pt \"Vladimir Script\";")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 48pt \"Vladimir Script\";")

        self.verticalLayout_3.addWidget(self.label_3)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        TicTacToe.setCentralWidget(self.centralwidget)

        self.retranslateUi(TicTacToe)

        QMetaObject.connectSlotsByName(TicTacToe)
    # setupUi

    def retranslateUi(self, TicTacToe):
        TicTacToe.setWindowTitle(QCoreApplication.translate("TicTacToe", u"MainWindow", None))
        self.pushButton_14.setText("")
        self.pushButton_17.setText("")
        self.pushButton_18.setText("")
        self.pushButton_15.setText("")
        self.pushButton_11.setText("")
        self.pushButton_16.setText("")
        self.pushButton_12.setText("")
        self.pushButton_10.setText("")
        self.pushButton_13.setText("")
        self.label.setText(QCoreApplication.translate("TicTacToe", u"TicTacToe", None))
        self.label_4.setText("")
        self.pushButton.setText(QCoreApplication.translate("TicTacToe", u"Reset game", None))
        self.pushButton_2.setText(QCoreApplication.translate("TicTacToe", u"Close", None))
        self.label_2.setText(QCoreApplication.translate("TicTacToe", u"Current: X", None))
        self.label_3.setText(QCoreApplication.translate("TicTacToe", u"Winner:", None))
    # retranslateUi

