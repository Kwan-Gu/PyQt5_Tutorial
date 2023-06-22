"""
QCheckBox 위젯은 on/off 두 상태를 갖는 버튼을 제공.
체크박스가 선택되거나 해제될 때, stateChanged() 시그널이 발생.
체크박스의 선택 여부를 확인하기 위해서 isChecked() 메서드를 사용 (선택 여부에 따라 boolean 값 반환).
setTristate() 메서드를 사용하면 '변경 없음' 상태를 가질 수 있음 (2/1/0).
체크박스의 상태를 얻기 위해서는 checkState() 메서드 사용.
여러 개의 버튼을 묶어서 exclusive / non-exclusive 버튼 그룹을 만들 수 있음 (exclusive 버튼 그룹은 여러 개 중 하나의 버튼만 선택 가능).
- 자주 사용되는 메서드.
    - text() : 체크박스의 라벨 텍스트 반환.
    - setText() : 체크박스의 라벨 텍스트를 설정.
    - isChecked() : 체크박스의 상태를 반환 (True / False).
    - checkState() : 체크박스의 상태를 반환 (2 / 1 / 0).
    - toggle() : 체크박스의 상태를 변경.
- 자주 사용되는 시그널.
    - pressed() : 체크박스를 누를 때 신호 발생.
    - released() : 체크박스를 뗄 때 신호 발생.
    - clicked() : 체크박스를 클릭할 때 신호 발생.
    - stateChanged() : 체크박스의 상태가 바뀔 때 신호 발생.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QDesktopWidget
from PyQt5.QtCore import Qt


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox("Change title", self)  # Show title이라는 텍스트 라벨을 갖는 체크박스를 생성
        cb.move(20, 20)
        # cb.toggle()
        cb.stateChanged.connect(self.changeTitle)  # 체크박스의 상태가 바뀔 때 발생하는 시그널을 changeTitle() 메서드에 연결

        # 창
        self.setWindowTitle("QCheckBox")
        self.center()
        self.resize(400, 300)
        self.show()

    def changeTitle(self, state):  # 체크박스의 상태가 changeTitle() 메서드의 매개변수
        if state == Qt.Checked:
            self.setWindowTitle("Checked")
        else:
            self.setWindowTitle("Non-Checked")

    def center(self):
        fg = self.frameGeometry()  # frameGeometry() 메서드를 이용해 창의 위치와 크기 정보를 가져옴
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악
        fg.moveCenter(cp)  # 창의 직사각형 위치를 화면의 중심 위치로 이동
        self.move(fg.topLeft())  # 현재 창을 화면의 중심으로 이동했던 fg의 위치로 이동


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
