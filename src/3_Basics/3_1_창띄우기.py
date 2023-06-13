"""
[참고 1]
moduleA.py 라는 코드를 import 해서 코드를 실행하면 __name__은 'moduleA'가 됨.
만약 코드를 직접 실행한다면 __name__은 __main__이 됨.
따라서 이 코드를 통해 프로그램이 직접 실행되는지 혹은 모듈을 통해 실행되는지 확인함.

[참고 2]
PyQt5에서의 이벤트 처리는 시그널과 슬롯 메커니즘으로 이루어짐.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        # [참고 2]
        btn = QPushButton('Quit', self)  # 첫번째 파라미터는 버튼에 표시될 텍스트, 두번째 파라미터는 버튼이 위치할 부모 위젯
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())  # sizeHint() 메서드는 버튼을 적절한 크기로 설정
        btn.clicked.connect(QCoreApplication.instance().quit)
        # 버튼을 클릭하면 clicked 시그널이 만들어짐
        # instance() 메서드는 현재 인스턴스를 반환
        # clicked 시그널은 quit 메서드에 연결
        # 발신자(btn)와 수신자(app) 두 객체 간에 커뮤니케이션이 이루어짐

        self.setWindowTitle("Baek's First Application")
        self.setWindowIcon(QIcon('../png/web.png'))
        # self.move(300, 300)  # 위젯을 스크린의 x=300 px, y=300 px의 위치로 이동
        # self.resize(400, 200)
        self.setGeometry(300, 300, 400, 200)  # 창의 위치와 크기를 설정 (x, y, w, h)
        self.show()


if __name__ == '__main__':  # __name__은 현재 모듈의 이름이 저장되는 내장 변수 (아래 [참고 1] 참고)
    app = QApplication(sys.argv)  # 모든 PyQt5 어플리케이션은 어플리케이션 객체를 생성해야 함.
    ex = MyApp()
    sys.exit(app.exec_())
