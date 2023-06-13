"""
QLabel 위젯은 텍스트 또는 이미지 라벨을 만들 때 사용.
사용자와 어떤 상호작용도 제공하지 않음.
기본적으로 수평 방향으로는 왼쪽 정렬, 수직 방향으로는 가운데 정렬이지만 setAlignment() 메서드를 통해 조절 가능.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QDesktopWidget
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # 라벨 생성
        lbl1 = QLabel("First Label", self)
        lbl1.setAlignment(Qt.AlignCenter)  # Qt.AlignCenter로 설정하면 수평, 수직 방향 모두 가운데 정렬
        
        lbl2 = QLabel("Second Label", self)
        lbl2.setAlignment(Qt.AlignVCenter)  # 수직 방향으로만 가운데 정렬(Qt.AlignVCenter)

        # 라벨 폰트
        font1 = lbl1.font()
        font1.setPointSize(20)  # setPointSize() 메서드로 폰트 크기 설정(default=13)
        
        font2 = lbl2.font()
        font2.setFamily("Times New Roman")  # 폰트 종류 설정
        font2.setBold(True)
        
        lbl1.setFont(font1)
        lbl2.setFont(font2)

        # 레이아웃
        lo = QVBoxLayout()
        lo.addWidget(lbl1)
        lo.addWidget(lbl2)

        self.setLayout(lo)

        # 창
        self.setWindowTitle("QLabel")
        self.center()
        self.resize(300, 300)
        self.show()

    def center(self):
        fg = self.frameGeometry()  # frameGeometry() 메서드를 이용해 창의 위치와 크기 정보를 가져옴
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악
        fg.moveCenter(cp)  # 창의 직사각형 위치를 화면의 중심 위치로 이동
        self.move(fg.topLeft())  # 현재 창을 화면의 중심으로 이동했던 fg의 위치로 이동


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
