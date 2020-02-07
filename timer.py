import sys
import winsound
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Timer(QMainWindow):

    def __init__(self):

        super().__init__()

        #表示する秒数
        self.time = 180
        #カウント中か
        self.run  = False

        self.initUI()


    def initUI(self):

        #ボタン(開始/停止)
        self.btn = QPushButton('スタート', self)
        self.btn.setGeometry(240, 20, 51, 21)
        self.btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn.clicked.connect(self.btnPushed)

        #ダイアル(時間を設定)
        self.dial = QDial(self)
        self.dial.setGeometry(240, 50, 51, 71)
        self.dial.setCursor(QCursor(Qt.PointingHandCursor))
        self.dial.setMinimum(1)
        self.dial.setMaximum(600)
        self.dial.setValue(self.time)
        self.dial.valueChanged.connect(self.turned)

        #ラベル(時間を表示)
        self.lbl = QLabel('03:00', self)
        self.lbl.setGeometry(10, 20, 221, 101)
        font = QFont()#ラベルのフォント
        font.setFamily("UD デジタル 教科書体 N-R")
        font.setPointSize(65)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.lbl.setFont(font)

        #カウンタ(UIではない)
        self.counter = QTimer()
        self.counter.setInterval(1000)#[msec]
        self.counter.timeout.connect(self.counted)

        #このウィンドウ
        self.setWindowTitle('タイマー')
        self.setGeometry(100, 100, 300, 182)
        self.setMinimumHeight(182)
        self.setMinimumWidth(300)
        self.setMaximumHeight(182)
        self.setMaximumWidth(300)

        self.show()


    def btnPushed(self):

        if self.run:
            self.run = False
            self.btn.setText('スタート')
            self.dial.setEnabled(True)
            self.counter.stop()

        else:
            self.run = True
            self.btn.setText('ストップ')
            self.dial.setEnabled(False)
            self.counter.start()


    def counted(self):

        if self.time > 0:
            self.time -= 1
        else:
            winsound.PlaySound('SystemExit', winsound.SND_ALIAS)


        m = self.time // 60
        s = self.time %  60

        self.lbl.setText('%02d:%02d' % (m, s))


    def turned(self):

        self.time = self.dial.value()

        m = self.time // 60
        s = self.time %  60

        self.lbl.setText('%02d:%02d' % (m, s))



if __name__ == '__main__':

    app = QApplication(sys.argv)
    timer = Timer()
    sys.exit(app.exec_())
