"""
일반적인 레이아웃 클래스는 그리드 레이아웃(Grid layout).
위젯의 공간을 행과 열로 구분.
그리드 레이아웃을 생성하기 위해 QGridLayout 클래스를 사용.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QDesktopWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel("Title:" ), 0, 0)  # addWidget() 메서드의 첫번째 파라미터는 추가할 위젯, 두/세번째 파라미터는 행/열
        grid.addWidget(QLabel("Author:"), 1, 0)
        grid.addWidget(QLabel("Review:"), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)  # QTextEdit() 위젯은 QLineEdit() 위젯과 달리 여러 줄의 텍스트를 수정

        # 창
        self.setWindowTitle("QGridLayout")
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
