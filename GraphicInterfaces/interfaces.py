
from PyQt5.QtWidgets import (
    QWidget, QFormLayout,
    QLabel, QLineEdit, QComboBox, QPushButton, QButtonGroup
)
from PyQt5.QtCore import Qt

class LayoutEditorForm(QWidget):
    '''
    Parametrs defining part
    '''
    def __init__(self, display) -> None:
        super().__init__()

        self.display = display

        self.initUI()


    def initUI(self):
        '''
        Creating form view
        '''
        # Defining layout
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # adding content
        layer_search = QLineEdit()
        self.layout.addRow(layer_search)
        layer_search.textChanged[str].connect(self.update_layer_btns_list)

        self.btns = {}
        self.btn_grp = QButtonGroup()
        self.btn_grp.buttonClicked[int].connect(self.layer_selected)
        id = 0
        for layer in self.display.get_layers():
            btn = QPushButton(layer)
            self.btn_grp.addButton(btn, id)
            id += 1
            self.btns[layer] = btn
            self.layout.addRow(btn)
            pass

    def update_layer_btns_list(self, text):
        ''''''
        for btn_name in self.btns.keys():
            if btn_name.startswith(text):
                self.btns[btn_name].show()
            else:
                self.btns[btn_name].hide()

    def layer_selected(self, text):
        ''''''
        for btn in self.btn_grp.buttons():
            if btn is self.btn_grp.button(text):
                self.display.set_draw_layer(btn.text())
        pass

    def updateDisplayView(self):
        ''''''
        print('clicked', self.w_inp.text())
        txt = self.w_inp.text()
        try:
            w = int(txt)
            self.display.r.setWidth(w)
            self.display.update()
        except:
            print(txt, 'not num')
            for atr in dir(Qt):
                if atr.endswith(txt):
                    print(atr)
            print('*'*50)