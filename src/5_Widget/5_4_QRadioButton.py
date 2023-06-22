"""
라디오버튼은 사용자에게 여러 개 중 하나의 옵션을 선택하도록 할 때 사용.
한 위젯 안에 여러 라디오버튼은 autoExclusive로 설정되어 있음 (하나의 버튼을 선택하면 나머지 버튼들은 선택 해제 됨).
한 번에 여러 버튼을 선택할 수 있도록 하려면 setAutoExclusive() 메서드에 False를 입력하면 됨.
한 위젯 안에 여러 개의 exclusive 버튼 그룹을 배치하고 싶다면, QButtonGroup() 메서드를 사용.
버튼의 상태가 바뀔 때 toggled() 시그널 발생.
특정 버튼의 상태를 가져오고 싶을 때 isChecked() 메서드를 사용.
- 자주 사용하는 메서드.
    - text() : 버튼의 텍스트 반환.
    - setText() : 라벨에 들어갈 텍스트 설정.
    - setChecked() : 버튼의 선택 여부 설정.
    - isChecked() : 버튼의 선택 여부 반환.
    - toggle() : 버튼의 상태 변경.
- 자주 사용하는 시그널.
    - pressed() : 버튼을 누를 때 신호 발생.
    - released() : 버튼에서 뗄 때 신호 발생.
    - clicked() : 버튼을 클릭할 때 신호 발생.
    - toggled() : 버튼의 상태가 바뀔 때 신호 발생.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QDesktopWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1 = QRadioButton("First Button", self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)  # setChecked()를 True로 설정하면 프로그램이 실행될 때 버튼이 선택되어 표시됨

        rbtn2 = QRadioButton("Second Button", self)
        rbtn2.move(50, 70)

        # 창
        self.setWindowTitle("QRadioButton")
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
