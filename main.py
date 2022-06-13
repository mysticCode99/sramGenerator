
from curses import window
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

from GraphicInterfaces.main_widget import Main_Widget
from VLSI.work_area import WorkArea

class Window(QMainWindow):
    def __init__(self, workdir):
        super().__init__()
        self.initUI(workdir)
        self.show()
    
    def initUI(self, workdir):
        width = 1000
        height = 500
        self.setGeometry(100, 100, width, height)

        window = Main_Widget(workdir)
        self.setCentralWidget(window)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    workdir = WorkArea()
    win = Window(workdir=workdir)
    win.show()
    sys.exit(app.exec_())