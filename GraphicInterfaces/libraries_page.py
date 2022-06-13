
from PyQt5.QtWidgets import (
    QWidget, QDialog, QHBoxLayout, QGridLayout, QVBoxLayout,
    QDialogButtonBox, QSizePolicy, QMenu,
    QComboBox, QLabel, QLineEdit, QButtonGroup,
    QPushButton, QListWidget
)
from PyQt5.QtCore import Qt, QSize


class Library(QWidget):
    ''''''
    def __init__(self, workdir):
        super().__init__()
        self.workdir = workdir
        self.initUI()
        self.lib_btns = QButtonGroup()
        self.blk_btns = QButtonGroup()
        self.cell_btns = QButtonGroup()
    
    def initUI(self):
        ''''''
        layout = QHBoxLayout()

        # lib list
        self.lib_list_lay = QVBoxLayout()
        self.lib_search = QLineEdit()
        self.lib_list = QListWidget()
        self.lib_list.itemClicked.connect(self.selected_lib)
        self.lib_list.addItems(self.workdir.get_libs())
        self.lib_list_lay.addWidget(QLabel('Libs list'))
        self.lib_list_lay.addWidget(self.lib_search)
        self.lib_list_lay.addWidget(self.lib_list)
        layout.addLayout(self.lib_list_lay, 25)

        # block list
        self.block_list_lay = QVBoxLayout()
        self.block_search = QLineEdit()
        self.block_list = QListWidget()
        self.block_list.itemClicked.connect(self.selected_block)
        self.block_list_lay.addWidget(QLabel('Blocks list'))
        self.block_list_lay.addWidget(self.block_search)
        self.block_list_lay.addWidget(self.block_list)
        layout.addLayout(self.block_list_lay, 25)

        # cell list
        self.cell_list_lay = QVBoxLayout()
        self.cell_search = QLineEdit()
        self.cell_list = QListWidget()
        self.cell_list.itemClicked.connect(self.selected_cell)
        self.cell_list_lay.addWidget(QLabel('Cells list'))
        self.cell_list_lay.addWidget(self.cell_search)
        self.cell_list_lay.addWidget(self.cell_list)
        layout.addLayout(self.cell_list_lay, 25)

        # view list
        self.view_list = QVBoxLayout()
        layout.addLayout(self.view_list, 25)

        # Adding compile layout
        self.setLayout(layout)

    def selected_lib(self, lib):
        '''Add blocks to block list when chosed lib'''
        self.selected_lib_name = lib.text()
        self.block_list.clear()
        lib_data = self.workdir.libs_data[self.selected_lib_name]
        self.block_list.addItems(lib_data['blocks'])

    def selected_block(self, block):
        '''Add blocks to block list when chosed lib'''
        self.selected_block_name = block.text()
        self.cell_list.clear()
        block_list = self.workdir.libs_data[self.selected_lib_name]['blocks'][self.selected_block_name]
        self.cell_list.addItems(block_list['cells'])

    def selected_cell(self, cell):
        '''Add blocks to block list when chosed lib'''

    def contextMenuEvent(self, event): 
        contextMenu = QMenu(self)
        add_lib = contextMenu.addAction("Add Library")
        add_block = contextMenu.addAction("Add Block")
        add_cell = contextMenu.addAction("Add Cell")
        copy = contextMenu.addAction("Copy")
        move = contextMenu.addAction("Move")
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == add_lib:
            print('Adding new library')
            win = Edit_Library_List(self, 'add lib')
            win.show()
        if action == add_block:
            win = Edit_Library_List(self, 'add block')
            print('Opening exist library')
        if action == add_cell:
            win = Edit_Library_List(self, 'add cell')
            print('Opening exist library')

    def add_lib(self, lib_name):
        '''Adding library'''
        self.lib_list.addItem(lib_name)
        self.workdir.add_lib(lib_name)
    
    def add_block(self, lib_name, block_name):
        '''Adding block'''
        self.block_list.addItem(block_name)
        self.workdir.add_block(lib_name, block_name)

    def add_cell(self, lib_name, block_name, cell_name):
        '''Adding cell'''
        self.cell_list.addItem(cell_name)
        self.workdir.add_cell(lib_name, block_name, cell_name)

class Edit_Library_List(QDialog):
    def __init__(self, root, mode) -> None:
        super().__init__(root)
        self.root_widget = root
        self.mode = mode
        self.libs_data = self.root_widget.workdir.libs_data
        self.setFixedSize(QSize(-1, -1))
        self.initUI()
    
    def initUI(self):
        '''Initilisation of UI'''
        self.setWindowTitle(self.mode.title())
        # self.setGeometry(self.left, self.top, 400, 100)
        self.mainLay = QVBoxLayout()
        selectLay = QGridLayout()
        self.sizeHint()

        self.name = QLineEdit()
        self.libsb = QComboBox()
        self.libsb.addItems(self.libs_data.keys())
        self.blocksb = QComboBox()
        lb_name = self.libsb.currentText()
        self.blocksb.addItems(self.libs_data[lb_name]['blocks'].keys())
        
        if self.mode == 'add lib':
            selectLay.addWidget(QLabel('Enter lib name'), 1, 1)
            selectLay.addWidget(self.name, 1, 2)
        elif self.mode == 'add block':
            selectLay.addWidget(QLabel('Choose lib'), 1, 1)
            selectLay.addWidget(QLabel('Enter block name'), 1, 2)
            selectLay.addWidget(self.libsb, 2, 1)
            selectLay.addWidget(self.name, 2, 2)
        elif self.mode == 'add cell':
            selectLay.addWidget(QLabel('Choose lib'), 1, 1)
            selectLay.addWidget(QLabel('Choose block'), 1, 2)
            selectLay.addWidget(QLabel('Enter cell name'), 1, 3)
            selectLay.addWidget(self.libsb, 2, 1)
            selectLay.addWidget(self.blocksb, 2, 2)
            selectLay.addWidget(self.name, 2, 3)
        
        # setting up accept and cencel btns
        self.btns = QDialogButtonBox()
        self.btns.setStandardButtons( 
            QDialogButtonBox.Ok |
            QDialogButtonBox.Cancel
        )
        self.btns.accepted.connect(self.accept)
        self.btns.rejected.connect(self.close)

        #Adding of Layout managers
        self.mainLay.addLayout(selectLay)
        self.mainLay.addWidget(self.btns)
        self.setLayout(self.mainLay)
        self.show()
    
    def accept(self):
        ''''''
        if self.mode == 'add lib':
            self.root_widget.add_lib(self.name.text())
        elif self.mode == 'add block':
            lib_name = self.libsb.currentText()
            block_name = self.name.text()
            self.root_widget.add_block(lib_name, block_name)
        elif self.mode == 'add cell':
            cell_name = self.name.text()
            print(cell_name)
            # self.root_widget.add_cell()
            pass
        self.close()