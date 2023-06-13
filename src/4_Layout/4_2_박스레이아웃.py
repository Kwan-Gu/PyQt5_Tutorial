"""
박스 레이아웃 클래스를 이용하면 유연하고 실용적인 레이아웃 구성 가능.
QHBoxLayout, QVBoxLayout은 여러 위젯을 수평, 수직으로 정렬하는 레이아웃 클래스.
QHBoxLayout, QVBoxLayout은 다른 레이아웃 박스를 넣을 수도 있고 위젯을 배치할 수도 있음.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QDesktopWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ok_btn = QPushButton("OK")
        cancel_btn = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)  # addStretch() 메서드는 유연한 빈 공간을 설정
        hbox.addWidget(ok_btn)
        hbox.addWidget(cancel_btn)
        hbox.addStretch(1)  # 두 버튼 양쪽의 stretch factor가 1로 같기 때문에 두 빈 공간의 크기는 창의 크기가 변해도 항상 동일

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)  # 수평 박스 위와 아래의 빈 공간 크기는 항상 3:1을 유지

        self.setLayout(vbox)  # 수직 박스를 창의 메인 레이아웃으로 설정

        # 창
        self.setWindowTitle("Box Layout")
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
