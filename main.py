import sys
from PyQt5.QtGui import QIcon
from ui_dokki_hotel_final_deploy import *


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Dokki Hotel")
        self.setWindowIcon(QIcon("hotelicosmall.ico"))
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
