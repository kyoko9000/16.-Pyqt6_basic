import sys
# pip install pyqt5
from PyQt6 import QtGui
from PyQt6.QtGui import QAction, QCursor
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMenu
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # tạo table với số hàng
        self.uic.tableWidget.setRowCount(10)

        # tạo table với số cột
        self.uic.tableWidget.setColumnCount(4)

        # paint color and write something
        self.uic.tableWidget.setItem(0, 1, QTableWidgetItem("hello"))
        self.uic.tableWidget.item(0, 1).setBackground(QtGui.QColor(0, 255, 0))

    def contextMenuEvent(self, event):
        self.menu = QMenu()
        renameAction = QAction('take value', self)
        renameAction1 = QAction('option 2', self)
        renameAction2 = QAction('option 3', self)

        self.menu.addAction(renameAction)
        self.menu.addAction(renameAction1)
        self.menu.addAction(renameAction2)
        # add other required actions
        self.menu.popup(QCursor.pos())
        renameAction.triggered.connect(self.take_value)

    def take_value(self):
        print("take value and position")
        # value and position
        currentItems = 0
        for currentItems in self.uic.tableWidget.selectedItems():
            print('row: ', currentItems.row())
            print("column: ", currentItems.column())
            print("value: ", currentItems.text())
        print(currentItems.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
