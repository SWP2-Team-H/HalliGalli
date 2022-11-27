import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from setting import *
from game import *

import display


class GameOption(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        titleText = QLabel("할리갈리")
        titleText.setFont(QtGui.QFont('Helvetica', 26))
        contentText = QLabel(
            "플레이어의 이름과 게임 시간을 입력한 후 게임모드를 선택하세요\n플레이어2의 이름은 로컬 멀티 플레이모드의 경우에만 입력하세요")
        soloText = QLabel("솔로 플레이")
        player1Text = QLabel("플레이어1")
        player2Text = QLabel("플레이어2")

        self.player1Edit = QLineEdit()
        self.player2Edit = QLineEdit()

        solo1Btn = QPushButton("EASY", self)
        solo2Btn = QPushButton("NORMAL", self)
        solo3Btn = QPushButton("HARD", self)
        option2Btn = QPushButton("통신 멀티 플레이", self)
        option3Btn = QPushButton("로컬 멀티 플레이", self)

        # 게임 타이틀, 중앙정렬을 위해 hbox사용
        hbox0 = QHBoxLayout()
        hbox0.addStretch(1)
        hbox0.addWidget(titleText)
        hbox0.addStretch(1)

        # 옵션 설명, 중앙정렬을 위해 hbox사용
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(contentText)
        hbox1.addStretch(1)

        # 솔로 플레이
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(soloText)

        # 플레이어1 이름 라벨, 입력칸
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(player1Text)
        hbox3.addWidget(self.player1Edit)

        # 플레이어2 이름 라벨, 입력칸
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(player2Text)
        hbox4.addWidget(self.player2Edit)

        # 플레이어1, 플레이어 2 수직 정렬
        vbox1 = QVBoxLayout()
        # vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)
        vbox1.addLayout(hbox4)

        # 옵션 버튼 수직 정렬
        vbox2 = QVBoxLayout()
        vbox2.addWidget(option2Btn)
        vbox2.addWidget(option3Btn)

        # 솔로 플레이 수평 정렬
        hbox5 = QHBoxLayout()
        hbox5.addStretch(1)
        hbox5.addLayout(hbox2)
        hbox5.addWidget(solo1Btn)
        hbox5.addWidget(solo2Btn)
        hbox5.addWidget(solo3Btn)
        hbox5.addStretch(1)

        # 각 항목과 버튼 수평 정렬
        hbox6 = QHBoxLayout()
        hbox6.addStretch(1)
        hbox6.addLayout(vbox1)
        hbox6.addLayout(vbox2)
        hbox6.addStretch(1)

        # 전체 레이아웃 수직 정렬
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox5)
        vbox.addLayout(hbox6)

        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('할리갈리')
        self.setLayout(vbox)
        self.show()

        # 버튼 연결
        solo1Btn.clicked.connect(self.solo1BtnClicked)
        solo2Btn.clicked.connect(self.solo2BtnClicked)
        solo3Btn.clicked.connect(self.solo3BtnClicked)
        option2Btn.clicked.connect(self.option2BtnClicked)
        option3Btn.clicked.connect(self.option3BtnClicked)

    # 솔로1 버튼 클릭시 실행될 함수
    def solo1BtnClicked(self):
        display.Display()

    # 솔로2 버튼 클릭시 실행될 함수
    def solo2BtnClicked(self):
        display.Display()

    # 솔로3 버튼 클릭시 실행될 함수
    def solo3BtnClicked(self):
        display.Display()

    # 옵션2 버튼 클릭시 실행될 함수
    def option2BtnClicked(self):
        global p_list
        p_list.clear()
        p_list.append(Player(self.player1Edit.text()))
        p_list.append(Player(self.player2Edit.text()))
        display.Display()

    # 옵션3 버튼 클릭시 실행될 함수
    def option3BtnClicked(self):
        display.Display()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GameOption()
    sys.exit(app.exec_())
