
from curses import window
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

from GraphicInterfaces.layout_editor import Layout_Editor

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    
    def initUI(self):
        width = 1000
        height = 500
        self.setGeometry(100, 100, width, height)

        window = Layout_Editor()
        self.setCentralWidget(window)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())