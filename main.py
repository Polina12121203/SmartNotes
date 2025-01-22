import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.widget)
        self.configure()
        
    def configure(self):
        self.ui.pushButton.clicked.connect(self.media_play)
        self.ui.pushButton_2.clicked.connect(self.media_stop)
        self.ui.calendarWidget.selectionChanged.connect(self.get_date)
        
        
    def get_date(self):
        num = str(self.ui.calendarWidget.selectedDate().day())
        self.media.setMedia(QMediaContent(QUrl.fromLocalFile(f'Video\\{num}.avi')))
        if self.ui.checkBox.isChecked:
            self.media.play()

    def media_play(self):
        self.media.play()

    def media_stop(self):
        self.media.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())