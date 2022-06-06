
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import (
    Qt, QRect, QPoint
)
from PyQt5.QtGui import (
    QPainter, QPen, QBrush
)

from VLSI.layers import Layer
from VLSI.config import layer_ordering, layers


class Painter(QWidget):
    ''''''
    def __init__(self, layers=layers) -> None:
        super().__init__()
        # configic karduma layerneri hertakanutyuny
        self.layer_ordering = layer_ordering
        # configic karduma layerneri kargavorumnery
        self.set_layers(layers)

        self.r = QRect()
        self.draw_layer_name = ''
        self.b = QBrush()
        self.begin, self.dest = QPoint(), QPoint()
        self.test_layers()

    def test_layers(self):
        x, y, w, h = 10, 10, 50, 50
        for layer_name in self.layer_ordering:
            if not self.layers.get(layer_name):
                continue
            self.layers[layer_name]['shapes'] = [QRect(x, y, w, h)]
            x += 10
            y += 10
        
        # adding layer named test
        self.layer_ordering.append('test')      # need for displayong
        self.layers['test'] = {}
        self.layers['test']['brush'] = QBrush()
        self.layers['test']['shapes'] = []
        self.update()
    
    def set_layers(self, layers):
        '''
        Read from dictionary layer params and add them
        '''
        self.layers = {}
        for layer in self.layer_ordering:
            self.layers[layer] = {
                'shapes' : [],
                'layer' : Layer(),
                'brush' : QBrush()
            }
        for layer_name, params in layers.items():
            self.set_layer(layer_name, params)
    
    def set_layer(self, layer_name, params):
        '''
        Defines Layer object and add to layer list
        '''
        layer = Layer(layer_name)
        layer.set_patern(params['color'], params['pattern'])
        self.layers[layer_name]['layer'] = layer
        self.layers[layer_name]['brush'] = QBrush(layer.color, layer.pattern)
    
    def set_draw_layer(self, layer_name):
        ''''''
        print('setting layer', layer_name)
        print(self.layers[layer_name])
        self.b = self.layers[layer_name]['brush']
        self.draw_layer_name = layer_name

    def get_layers(self):
        ''''''
        for layer in self.layer_ordering:
            yield layer

    def paintEvent(self, event):
        ''''''
        qp = QPainter(self)
        for layer in self.layer_ordering:
            shapes = self.layers[layer]['shapes']
            brush = self.layers[layer]['brush']
            qp.setBrush(brush)
            for shape in shapes:
                qp.drawRect(shape)
        qp.setBrush(self.b)
        # qp.drawRect(self.r.normalized())
    
    def mousePressEvent(self, event):
        '''
        Start drawing when pressed left button of mouse 
        '''
        if event.buttons() == Qt.LeftButton and self.draw_layer_name:
            self.r = QRect()
            self.r.setTopLeft(event.pos())
            self.r.setBottomRight(event.pos())
            self.layers[self.draw_layer_name]['shapes'].append(self.r)
        self.update()

    def mouseMoveEvent(self, event):
        '''
        Start drawing when pressed left button of mouse 
        '''
        if event.buttons() == Qt.LeftButton:
            self.r.setBottomRight(event.pos())
        self.e = event.pos()
        self.update()
    
    def mouseReleaseEvent(self, event):
        '''
        Adding rect to list 
        '''
        self.r = QRect()
        print('mouseReleaseEvent')
        self.update()