from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import gui


class ExampleApp(QtWidgets.QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

        header = self.table_global.horizontalHeader()
        for i in range(4):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = self.table_global.verticalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        header = self.table_career.horizontalHeader()
        for i in range(6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        header = self.table_career.verticalHeader()
        for i in range(6):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()