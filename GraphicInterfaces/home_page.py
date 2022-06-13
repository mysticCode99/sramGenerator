
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy,
    QPushButton, QLabel
)

from GraphicInterfaces.layout_editor import Layout_Editor
from GraphicInterfaces.libraries_page import Library

class Home_Tab(QWidget):
    ''''''
    def __init__(self, root_widget):
        super().__init__()
        self.root = root_widget
        self.initUI()
    
    def initUI(self):
        ''''''
        layout = QVBoxLayout()

        main_btns_list = QHBoxLayout()

        # main buttons
        lib_btn = QPushButton('Library')
        lib_btn.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        lib_btn.clicked.connect(lambda: self.root.add_tab(Library(self.root.workdir), 'Library'))
        main_btns_list.addWidget(lib_btn)
        sim_btn = QPushButton('Simulation')
        sim_btn.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        main_btns_list.addWidget(sim_btn)
        # main_btns_list.addWidget(QPushButton('Library'))

        # recent opened views
        last_opened_list = QHBoxLayout()
        last_opened = QPushButton('Last Opened Layout')
        last_opened.clicked.connect(lambda: self.root.add_tab(Layout_Editor(), 'Layout'))
        last_opened_list.addWidget(last_opened)

        layout.addLayout(main_btns_list)
        layout.addWidget(QLabel('Last opened'))
        layout.addLayout(last_opened_list)
        self.setLayout(layout)
        