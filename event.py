# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout,QDesktopWidget
# from PyQt5.QtGui import QIcon
#
# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#         grid = QGridLayout()
#         btn6 = QPushButton("Click 6")
#         grid.addWidget(btn6, 1, 1)
#         # specify the position
#
#         self.setLayout(grid)
#     def initUI(self):
#         self.setWindowTitle('Main')
#         self.resize(500,500)
#         self.center()
#         self.show()
#
#     def center(self):
#         qr=self.frameGeometry() #창의 위치와 크기 정보를 가져옴
#         cp=QDesktopWidget().availableGeometry().center() #사용하는 모니터 화면의 가운데 위치를 파악
#         qr.moveCenter(cp) #창의 직사각형 위치를 화면 중심의 위치로 이동
#         self.move(qr.topLeft()) #현재 창의 중심이 화면 중심과 일치
#
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())

import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
form_class = uic.loadUiType('DesignerMain.ui')[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pushButton.clicked.connect(self.close)

    def mousePressEvent(self, event) :
        if event.button() == Qt.LeftButton :
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event) :
        try:
            if self.offset is not None and event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.pos() - self.offset)
            else:
                super().mouseMoveEvent(event)
        except:
            pass

    def mouseReleaseEvent(self, event) :
        self.offset = None
        super().mouseReleaseEvent(event)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()