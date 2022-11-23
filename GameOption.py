import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

import display

class GameOption(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        titleText = QLabel("할리갈리")
        titleText.setFont(QtGui.QFont('Helvetica',26))
        contentText = QLabel("플레이어의 이름과 게임 시간을 입력한 후 게임모드를 선택하세요\n플레이어2의 이름은 로컬 멀티 플레이모드의 경우에만 입력하세요")
        player1Text = QLabel("플레이어1")
        player2Text = QLabel("플레이어2")
        timeText = QLabel("게임 시간(초)")
        
        self.player1Edit = QLineEdit()
        self.player2Edit = QLineEdit()
        self.timeEdit = QLineEdit()
        
        option1Btn = QPushButton("솔로 플레이", self)
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

        # 플레이어1 이름 라벨, 입력칸
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(player1Text)
        hbox2.addWidget(self.player1Edit)

        # 플레이어2 이름 라벨, 입력칸
        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        hbox3.addWidget(player2Text)
        hbox3.addWidget(self.player2Edit)

        # 게임 시간 라벨, 입력칸
        hbox4 = QHBoxLayout()
        hbox4.addStretch(1)
        hbox4.addWidget(timeText)
        hbox4.addWidget(self.timeEdit)

        # 플레이어1, 플레이어2, 게임시간 수직 정렬
        vbox1 = QVBoxLayout()
        vbox1.addLayout(hbox2)
        vbox1.addLayout(hbox3)
        vbox1.addLayout(hbox4)
        
        # 옵션 버튼 수직 정렬
        vbox2 = QVBoxLayout()
        vbox2.addWidget(option1Btn)
        vbox2.addWidget(option2Btn)
        vbox2.addWidget(option3Btn)
        
        # 각 항목과 버튼 수평 정렬
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addLayout(vbox1)
        hbox.addLayout(vbox2)
        hbox.addStretch(1)
        
        # 전체 레이아웃 수직 정렬
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox)

        self.setGeometry(300, 300, 500, 200)
        self.setWindowTitle('할리갈리')   
        self.setLayout(vbox)
        self.show()

        # 버튼 연결
        option1Btn.clicked.connect(self.option1BtnClicked)
        option2Btn.clicked.connect(self.option2BtnClicked)
        option3Btn.clicked.connect(self.option3BtnClicked)
        
    # 옵션1 버튼 클릭시 실행될 함수  
    def option1BtnClicked(self):
        display.Display()
    
    # 옵션2 버튼 클릭시 실행될 함수  
    def option2BtnClicked(self):
        display.Display()
        
    # 옵션3 버튼 클릭시 실행될 함수  
    def option3BtnClicked(self):
        display.Display()
        
if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = GameOption()
    sys.exit(app.exec_())

