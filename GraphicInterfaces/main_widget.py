
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QTabWidget,
)
from PyQt5.QtCore import Qt

from GraphicInterfaces.home_page import Home_Tab

class Main_Widget(QWidget):
    ''''''
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        ''''''
        layout = QVBoxLayout()
        self.tabs = QTabWidget(self)
        self.tabs.addTab(Home_Tab(self), 'Layout')
        layout.addWidget(self.tabs)
        self.setLayout(layout)
    
    def add_tab(self, widget, name):
        ''''''
        self.tabs.addTab(widget, name)