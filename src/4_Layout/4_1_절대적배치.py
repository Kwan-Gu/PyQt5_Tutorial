"""
레이아웃은 어플리케이션 창에 위젯들을 배치하는 방식.
PyQt5의 위젯들을 배치하는 방식에는 절대적 배치, 박스 레이아웃, 그리드 레이아웃이 있음.
- 절대적 배치(Absolute positioning) 방식은 각 위젯의 위치와 크기를 픽셀 단위로 설정해서 배치.
  - 창의 크기를 조절해도 위젯의 크기와 위치는 변하지 않음.
  - 플랫폼에 따라 어플리케이션이 다르게 보일 수 있음.
  - 폰트를 바꾸면 레이아웃이 망가질 수 있음.
  - 레이아웃을 바꾸고 싶다면 완전히 새로 고쳐야 함.
  - 좌표계는 왼쪽 상단 모서리에서 시작 (x좌표는 왼쪽에서 오른쪽으로 갈수록 커지고, y좌표는 위에서 아래로 갈수록 커짐).
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDesktopWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl1 = QLabel("Label1", self)
        lbl1.move(20, 20)
        lbl2 = QLabel("Label2", self)
        lbl2.move(20, 60)

        btn1 = QPushButton("Button1", self)
        btn1.move(80, 13)
        btn2 = QPushButton("Button2", self)
        btn2.move(80, 53)

        # 창
        self.setWindowTitle("Absolute Positioning")
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
