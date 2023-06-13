"""
메인창은(Main window)은 메뉴바, 툴바, 상태바를 갖는 어플리케이션 창 (mainwindowlayout.png).
메인창은 QMenuBar, QToolBar, QDockWidget, QStatusBar를 위한 고유의 레이아웃을 가짐.
또한 가운데 영역에 중심위젯(Central widget)을 위한 영역을 가지며, 여기에는 어떠한 위젯도 들어올 수 있음.
- 상태바(QStatusBar)는 어플리케이션의 상태를 알려주기 위해 어플리케이션의 하단에 위치하는 위젯.
  - 텍스트가 사라지게 하고 싶으면 clearMessage() 메서드를 사용하거나, showMessage() 메서드에서 텍스트가 표시되는 시간을 설정 가능.
  - 현재 상태바에 표시되는 메세지 텍스트를 갖고 오고 싶으면 currentMessage() 메서드를 사용.
  - QStatusBar 클래스는 상태바에 표시되는 메세지가 바뀔 때마다 messageChanged() 시그널을 발생시킴.
- 메뉴바(QMenuBar)는 다양한 명령들의 모음이 위치.
- 툴바(QToolBar)는 자주 사용하는 명령들을 편리하게 사용할 수 있도록 함.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, QDateTime, Qt


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()  # currentDate() 메서드를 통해 현재 날짜를 얻음
        # self.date = QDateTime.currentDateTime()
        self.initUI()

    def initUI(self):
        # 종료 액션
        exitAction = QAction(QIcon('../png/exit.png'), 'Exit', self)  # 아이콘과 'Exit' 라벨을 갖는 하나의 action을 구성
        exitAction.setShortcut('Ctrl+Q')  # 위 action에 단축키 정의
        exitAction.setStatusTip('Exit application')
        # 마우스를 올렸을 때 상태바에 나타날 상태팁을 setStatusTip() 메서드에 설정
        exitAction.triggered.connect(qApp.quit)

        # 메뉴바
        menubar = self.menuBar()  # menuBar() 메서드는 메뉴바를 생성
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        # 'File' 메뉴를 생성
        # '&File'의 앰퍼샌드(ampersand, &)는 간편하게 단축키를 설정하도록 함
        # 'F' 앞에 앰퍼샌드가 있으므로 'Alt+F'가 File 메뉴의 단축키
        filemenu.addAction(exitAction)  # exitAction 동작을 추가

        # 툴바
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)  # addAction() 메서드를 이용해서 툴바에 exitAction 동작을 추가

        # 상태바
        self.statusBar()
        # self.statusBar().showMessage('Ready', 2000)  # showMessage() 메서드를 통해 상태바에 보여질 메세지를 설정
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        # 창
        self.setWindowTitle("Baek's MainWindow")
        # self.setGeometry(2000, 300, 500, 350)
        self.resize(500, 350)
        self.center()  # 아래에서 정의한 center() 메서드를 통해 창이 화면의 중앙에 위치하게 됨
        self.show()

    def center(self):
        fg = self.frameGeometry()  # frameGeometry() 메서드를 이용해 창의 위치와 크기 정보를 가져옴
        cp = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치를 파악
        fg.moveCenter(cp)  # 창의 직사각형 위치를 화면의 중심 위치로 이동
        self.move(fg.topLeft())  # 현재 창을 화면의 중심으로 이동했던 fg의 위치로 이동


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
