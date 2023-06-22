"""
QComboBox는 여러 옵션들 중 하나의 옵션을 선택하는 위젯
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.lbl = None
        self.initUI()

    def initUI(self):
        self.lbl = QLabel("Option1", self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem("Option1")
        cb.addItem("Option2")
        cb.addItem("Option3")
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)  # 옵션을 선택하면 onActivated() 메서드가 호출됨

        self.setWindowTitle("QComboBox")
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()  # adjustSize() 메서드를 이용해 라벨의 크기를 자동으로 조절


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
