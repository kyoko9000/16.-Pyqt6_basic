# no need to install anything
import sys
# pip install pyqt5, pip install pyqt5 tools
from PyQt6.QtGui import QCursor, QAction
from PyQt6.QtWidgets import QMenu
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import QModelIndex
# just change the name
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.event = None
        self.menu = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        # tạo table với số hàng
        self.uic.tableWidget.setRowCount(10)
        # tạo table với số cột
        self.uic.tableWidget.setColumnCount(4)
        # ghi lên một ô bất kỳ
        self.uic.tableWidget.setItem(0, 3, QTableWidgetItem("hello"))
        # tạo thanh địa chỉ
        self.uic.tableWidget.setHorizontalHeaderLabels(['A1', 'A2', 'A3', 'A4', 'A5', 'A6'])
        # self.uic.tableWidget.setVerticalHeaderLabels(['', '', '', '', '', ''])

        # khai báo nút ấn
        self.uic.Button_add_row.clicked.connect(self.add_row)
        self.uic.Button_add_column.clicked.connect(self.add_column)
        self.uic.Button_remove_row.clicked.connect(self.remove_row)
        self.uic.Button_remove_column.clicked.connect(self.remove_column)
        self.uic.Button_read_cell.clicked.connect(self.read_cell)

        # paint color and write something
        self.uic.tableWidget.setItem(0, 1, QTableWidgetItem("gl"))
        self.uic.tableWidget.item(0, 1).setBackground(QtGui.QColor(100, 100, 150))

    # đọc từ một ô bất kỳ
    def read_cell(self):
        try:
            a = self.uic.tableWidget.item(0, 0).text()
            print(a)
        except:
            print("empty")

    def add_row(self):
        # row_bottom = self.uic.tableWidget.rowCount()
        current_row = self.uic.tableWidget.currentRow()
        self.uic.tableWidget.insertRow(current_row)

    def remove_row(self):
        # row_bottom = self.uic.tableWidget.rowCount()
        current_row = self.uic.tableWidget.currentRow()
        self.uic.tableWidget.removeRow(current_row)

    def add_column(self):
        # column_bottom = self.uic.tableWidget.columnCount()
        current_column = self.uic.tableWidget.currentColumn()
        self.uic.tableWidget.insertColumn(current_column)
        self.uic.tableWidget.setHorizontalHeaderLabels(['A1', 'A2', 'A3', 'A4', 'A5', 'A6'])

    def remove_column(self):
        # column_bottom = self.uic.tableWidget.columnCount()
        current_column = self.uic.tableWidget.currentColumn()
        self.uic.tableWidget.removeColumn(current_column)
        self.uic.tableWidget.setHorizontalHeaderLabels(['A1', 'A2', 'A3', 'A4', 'A5', 'A6'])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
