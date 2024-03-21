# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'howToPlay.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1087, 579)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.howToPlayHorizontalLayout = QHBoxLayout()
        self.howToPlayHorizontalLayout.setObjectName(u"howToPlayHorizontalLayout")
        self.howToPlayHorizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.howToPlayHorizontalLayout.addItem(self.horizontalSpacer)

        self.howToPlayTitleLabel = QLabel(Dialog)
        self.howToPlayTitleLabel.setObjectName(u"howToPlayTitleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.howToPlayTitleLabel.sizePolicy().hasHeightForWidth())
        self.howToPlayTitleLabel.setSizePolicy(sizePolicy)
        self.howToPlayTitleLabel.setMaximumSize(QSize(300, 50))
        font = QFont()
        font.setPointSize(24)
        self.howToPlayTitleLabel.setFont(font)
        self.howToPlayTitleLabel.setLayoutDirection(Qt.LeftToRight)

        self.howToPlayHorizontalLayout.addWidget(self.howToPlayTitleLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.howToPlayHorizontalLayout.addItem(self.horizontalSpacer_2)

        self.howToPlayReturnButton = QPushButton(Dialog)
        self.howToPlayReturnButton.setObjectName(u"howToPlayReturnButton")
        sizePolicy.setHeightForWidth(self.howToPlayReturnButton.sizePolicy().hasHeightForWidth())
        self.howToPlayReturnButton.setSizePolicy(sizePolicy)
        self.howToPlayReturnButton.setMinimumSize(QSize(200, 50))
        self.howToPlayReturnButton.setMaximumSize(QSize(200, 60))
        font1 = QFont()
        font1.setPointSize(16)
        self.howToPlayReturnButton.setFont(font1)

        self.howToPlayHorizontalLayout.addWidget(self.howToPlayReturnButton)


        self.gridLayout.addLayout(self.howToPlayHorizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1042, 1162))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.howToPlayInfo = QLabel(self.scrollAreaWidgetContents)
        self.howToPlayInfo.setObjectName(u"howToPlayInfo")
        self.howToPlayInfo.setMinimumSize(QSize(0, 250))
        self.howToPlayInfo.setSizeIncrement(QSize(1000, 1000))
        self.howToPlayInfo.setBaseSize(QSize(500, 500))
        font2 = QFont()
        font2.setPointSize(12)
        self.howToPlayInfo.setFont(font2)
        self.howToPlayInfo.setAutoFillBackground(False)
        self.howToPlayInfo.setFrameShape(QFrame.Box)
        self.howToPlayInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.howToPlayInfo.setWordWrap(True)

        self.gridLayout_2.addWidget(self.howToPlayInfo, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.howToPlayTitleLabel.setText(QCoreApplication.translate("Dialog", u"How To Play", None))
        self.howToPlayReturnButton.setText(QCoreApplication.translate("Dialog", u"Return", None))
        self.howToPlayInfo.setText(QCoreApplication.translate("Dialog", u"- The program will act as the \u2018bank\u2019 in the traditional board games, in charge of transferring funds and properties between the players of the game.\n"
"- The objective of the game is to become the wealthiest player, bankrupting all other opponents through means of buying, renting, and selling of property.\n"
"- Players are all given the same amount of money at the start of the game and are all placed on the starting tile on a board with 40 tiles.\n"
"- The board\u2019s shape is square, with 10 tiles on each side, with space in the centre of the board to display various objects.\n"
"- The board\u2019s layout contains 22 coloured properties, 4 railroads, 2 utilities, 6 \u2018chance/community chest\u2019 spaces, 2 tax spaces, 1 starting tile, 1 \u2018free parking\u2019 space, 1 go to jail space and 1 in jail/visiting space.\n"
"	o The coloured properties are distributed in colour groups of 2 or 3, each with specified rents and names. Each coloured property has indicators on the top of them to show the "
                        "number of houses owned on that property.\n"
"	o Railroads are placed in the midpoints of each side of the board, with rents depending on the number of railroads owned by a player.\n"
"	o Utilities are placed close to opposite sides of the board, with rents being a multiple of a user\u2019s roll, with this multiplicative value depending on the number of utilities owned by a player. (Rento does not contain utilities, but the created 	  solution to the problem will.)\n"
"- The names of the properties are named to follow an animal theme, with their names and costs being displayed on the tile if they are purchasable. the colour of the player who owns that property and whether that property is mortgaged or not is indicated on each property.\n"
"- Players will use random dice rolls to determine the number of squares they will move forwards each turn. They can click the dice at the start of their turns, as well as choose to mortgage properties, trade or buy houses.\n"
"- If players get a certain number of doubles in s"
                        "uccession, they will be sent to jail.\n"
"- Multiple players are able to reside on one tile at a time.\n"
"- Each time a player passes or lands on the starting tile, they gain fixed amounts of money, specified in the pre-game settings menu.\n"
"- Depending on the tile reached, players will perform a variety of actions, such as purchasing property, paying rent, paying taxes and drawing \u2018chance\u2019 cards.\n"
"	o When landing on unowned properties, players may buy the property at its indicated price, and will subsequently own it, entitling them to tax if others land on their property.\n"
"	o When landing on properties owned by others, the owner of the property collects rent as specified by the property. Rent can be increased through the purchasing of houses and or hotels, once a player has all of the properties from a colour group.\n"
"	o When landing on \u2018chance\u2019 tiles, a random card is given to the player which can either reward them or set them back.\n"
"	o Tax spaces require the user to pay fi"
                        "xed amounts of money to the bank.\n"
"	o The \u2018go to jail\u2019 space will send the user to jail, where the user can be held for several turns, still being able to collect rent if the setting is enabled, and purchase houses and/or hotels.\n"
"	o The free parking tile acts as a resting place for users, with users able to receive rewards for landing on it depending on the rules of the specific game.\n"
"- Houses and/or hotels can be purchased once a user has completed a colour set, with fixed pricings, in order to increase the rent amount to known values. They can also be sold by the users.\n"
"- Properties can be mortgaged by a user to the bank at the start or end of a player's turn. No rent is collected by a mortgaged property, and the owner of the mortgaged card may pay the bank to lift the mortgage.\n"
"- Players lose and are declared bankrupt when they owe more than they can pay either to another player, or to the bank. Assets of the bankrupted player are transferred to the player (or bank) who bankrupt"
                        "s another player.", None))
    # retranslateUi

