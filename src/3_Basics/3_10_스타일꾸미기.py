import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QDesktopWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QLabel 클래스를 이용해 라벨 위젯 생성
        lbl_red = QLabel('Red')  # 라벨 텍스트
        lbl_grn = QLabel('Green')
        lbl_blu = QLabel('Blue')

        lbl_red.setStyleSheet("color:red;"  # 글자색
                              "border-style:solid;"  # 경계선 스타일
                              "border-width:2px;"  # 경계선 두께
                              "border-color:#FA8072;"  # 경계선 색
                              "border-radius:3px;")  # 경계선 모서리 둥근 정도
        lbl_grn.setStyleSheet("color:green;"
                              "background-color:#7FFFD4;")  # 배경색
        lbl_blu.setStyleSheet("color:blue;"
                              "background-color:#87CEFA;"
                              "border-style:dashed;"
                              "border-width:3px;"
                              "border-color:#1E90FF;")

        vbox = QVBoxLayout()  # 수직 박스 레이아웃(QVBoxLayout())을 이용해 수직으로 배치 예정
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_grn)
        vbox.addWidget(lbl_blu)

        self.setLayout(vbox)

        # 창
        self.setWindowTitle("StyleSheet")
        self.resize(300, 300)
        self.center()
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
