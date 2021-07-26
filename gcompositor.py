from os import listdir
from sys import argv, exit

from PyQt5.Qt import *


class GC:
    def __init__(self):
        self.app = QApplication(argv)
        self.ferramentas = QWidgets()

    def janelaPrincipal(self):
        pass


if __name__ == '__main__':
    gcApp = GC()
    gcApp.ferramentas.show()
    gcApp.app.exec_()
