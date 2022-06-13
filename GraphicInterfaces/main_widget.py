
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget,
)
from PyQt5.QtCore import Qt

from GraphicInterfaces.home_page import Home_Tab

class Main_Widget(QWidget):
    ''''''
    def __init__(self, workdir):
        super().__init__()
        self.workdir = workdir
        self.initUI()
    
    def initUI(self):
        ''''''
        layout = QVBoxLayout()

        # setting up tab widget
        self.tabs = QTabWidget(self)
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested[int].connect(self.delete_tab)

        # adding home tab
        self.tabs.addTab(Home_Tab(self), 'Home')
        layout.addWidget(self.tabs)
        self.setLayout(layout)
    
    def add_tab(self, widget, name):
        ''''''
        self.tabs.addTab(widget, name)
        index = self.tabs.indexOf(widget)
        self.tabs.setCurrentIndex(index)
    
    def delete_tab(self, index):
        ''''''
        if index != 0:
            self.tabs.removeTab(index)
        if self.tabs.count() == 0:
            self.close()