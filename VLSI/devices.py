



class Device(object):
    """"""
    def __init__(self) -> None:
        super().__init__()
        self.layers = {
            'diff' : [],
            'poly' : [],
            'cont' : [],
            'met1' : []
        }
        pass

    def createPhysicalView(self):
        ''''''
        pass

class MosFet(Device):
    """"""
    def __init__(self) -> None:
        self.createPhysicalView()
        pass

    def createPhysicalView(self):
        ''''''
        # s_diff = Layer(50, 50, 50, 50)
        # d_diff = Layer(110, 50, 50, 50)
        # gate = Layer(100, 10, 10, 130)
        # self.layers['diff'].extend(s_diff, d_diff)
        # self.layers['poly'].append(gate)
        pass