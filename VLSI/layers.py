
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QColor

class Layer(object):
    """"""
    def __init__(self, name='') -> None:
        super().__init__()
        self.name = name
        self.pattern = Qt.SolidPattern
        self.color = QColor(0,0,0,1)

    def __str__(self) -> str:
        return self.name

    def set_patern(self, color, pattern_name):
        ''''''
        self.color = QColor(color)
        if pattern_name == 'SolidPattern' or pattern_name == '':
            self.pattern = Qt.SolidPattern
        elif pattern_name == 'BDiagPattern':
            self.pattern = Qt.BDiagPattern
        elif pattern_name == 'ConicalGradientPattern':
            self.pattern = Qt.ConicalGradientPattern
        elif pattern_name == 'CrossPattern':
            self.pattern = Qt.CrossPattern
        elif pattern_name == 'Dense1Pattern':
            self.pattern = Qt.Dense1Pattern
        elif pattern_name == 'Dense2Pattern':
            self.pattern = Qt.Dense2Pattern
        elif pattern_name == 'Dense3Pattern':
            self.pattern = Qt.Dense3Pattern
        elif pattern_name == 'Dense4Pattern':
            self.pattern = Qt.Dense4Pattern
        elif pattern_name == 'Dense5Pattern':
            self.pattern = Qt.Dense5Pattern
        elif pattern_name == 'Dense6Pattern':
            self.pattern = Qt.Dense6Pattern
        elif pattern_name == 'Dense7Pattern':
            self.pattern = Qt.Dense7Pattern
        elif pattern_name == 'DiagCrossPattern':
            self.pattern = Qt.DiagCrossPattern
        elif pattern_name == 'FDiagPattern':
            self.pattern = Qt.FDiagPattern
        elif pattern_name == 'HorPattern':
            self.pattern = Qt.HorPattern
        elif pattern_name == 'LinearGradientPattern':
            self.pattern = Qt.LinearGradientPattern
        elif pattern_name == 'RadialGradientPattern':
            self.pattern = Qt.RadialGradientPattern
        elif pattern_name == 'TexturePattern':
            self.pattern = Qt.TexturePattern
        elif pattern_name == 'VerPattern':
            self.pattern = Qt.VerPattern
        else:
            self.pattern = Qt.SolidPattern