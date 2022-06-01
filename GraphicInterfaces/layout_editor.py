
from PyQt5.QtWidgets import (
    QWidget, QHBoxLayout, QFormLayout
)
from PyQt5.QtGui import (
    QPainter
)

from GraphicInterfaces.Display import Painter
from GraphicInterfaces.interfaces import LayoutEditorForm


class Layout_Editor(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.initUI()

    def initUI(self):
        ''''''
        # Basic setups
        width = 1000
        height = 500
        self.setGeometry(100, 100, width, height)
        self.setWindowTitle('Layout Editor')

        # view layout setup
        main_layout = QHBoxLayout()

        display = Painter()
        interface = LayoutEditorForm(display)

        # assembling view in main layout
        main_layout.addWidget(display, 1)
        main_layout.addWidget(interface, 0)
        self.setLayout(main_layout)
        pass