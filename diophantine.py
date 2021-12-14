# from math import *
from PyQt5.QtWidgets import QInputDialog, QWidget, QApplication, QLabel
from PyQt5.QtCore import Qt
import sys

class Diophantine(QWidget):
    def __init__(self):
        self.variables = []
        super().__init__()
    def set_values(self):
        names = ['A', 'B', 'C']
        for name in names:
            ret = QInputDialog.getInt(self, 'Diophantine', name)
            self.variables.append(ret[0])
    def get_values(self):
        return self.variables
    # def display_values(self, m, n):
    #     self.setWindowTitle("Diophantine")
    #     label = QLabel(f"a:{m}  b:{n}")
    #     label.setAlignment(Qt.AlignCenter)
    #     self.setCentralWidget(label)


def solve_Diophantine(a, b, c):
    m1 = 1
    m2 = 0
    n1 = 0
    n2 = 1
    r1 = a
    r2 = b
    while r1 % r2 != 0:
        q = r1 // r2
        aux = r1 % r2
        r1 = r2
        r2 = aux
        aux3 = n1 - (n2 * q)
        aux2 = m1 - (m2 * q)
        m1 = m2
        n1 = n2
        m2 = aux2
        n2 = aux3
    return m2 * c, n2 * c


def main():
    dioph.set_values()
    a, b, c = dioph.get_values()
    m2, n2 = solve_Diophantine(a, b, c)
    # dioph.display_values(m2, n2)
    print(m2, n2)

if __name__ == '__main__':
    # print(sys.argv)

    app = QApplication([''])
    dioph = Diophantine()
    main()