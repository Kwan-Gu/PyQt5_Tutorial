"""
푸시버튼은 사용자가 프로그램에 명령을 내려서 어떤 동작을 하도록 할 때 사용되는 버튼.
- 자주 사용되는 메서드.
    - setCheckable() : True 설정 시, 누른 상태와 그렇지 않은 상태를 구분.
    - toggle() : 상태를 바꿈.
    - setIcon() : 버튼의 아이콘을 설정.
    - setEnabled() : False 설정 시, 버튼을 사용할 수 없음.
    - isChecked() : 버튼의 선택 여부를 반환.
    - setText() : 버튼에 표시될 텍스트를 설정.
    - text() : 버튼에 표시된 텍스트를 반환.
- 자주 사용되는 시그널.
    - clicked()  : 버튼을 클릭할 때 발생.
    - pressed()  : 버튼이 눌렸을 때 발생.
    - released() : 버튼을 눌렀다 뗄 때 발생.
    - toggled()  : 버튼의 상태가 바뀔 때 발생.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDesktopWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 버튼 정의
        btn1 = QPushButton("&Button1", self)  # 첫번째 파라미터는 버튼에 나타날 텍스트, 두번째 파라미터는 버튼이 속할 부모 클래스
        btn1.setCheckable(True)
        btn1.toggle()
        # toggle() 메서드를 호출하면 버튼의 상태가 바뀜
        # 이 버튼은 프로그램이 시작될 때 선택되어 있음
        
        btn2 = QPushButton(self)
        btn2.setText("Button&2")

        btn3 = QPushButton("Button3", self)
        btn3.setEnabled(False)

        # 레이아웃
        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        # 창
        self.setLayout(vbox)
        self.setWindowTitle("QPushButton")
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