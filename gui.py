# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(779, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 621, 301))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AnyKeyPressed|QtWidgets.QAbstractItemView.EditTrigger.DoubleClicked|QtWidgets.QAbstractItemView.EditTrigger.EditKeyPressed)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.Button_add_row = QtWidgets.QPushButton(self.centralwidget)
        self.Button_add_row.setGeometry(QtCore.QRect(50, 330, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_add_row.setFont(font)
        self.Button_add_row.setObjectName("Button_add_row")
        self.Button_remove_row = QtWidgets.QPushButton(self.centralwidget)
        self.Button_remove_row.setGeometry(QtCore.QRect(250, 330, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_remove_row.setFont(font)
        self.Button_remove_row.setObjectName("Button_remove_row")
        self.Button_remove_column = QtWidgets.QPushButton(self.centralwidget)
        self.Button_remove_column.setGeometry(QtCore.QRect(250, 410, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_remove_column.setFont(font)
        self.Button_remove_column.setObjectName("Button_remove_column")
        self.Button_add_column = QtWidgets.QPushButton(self.centralwidget)
        self.Button_add_column.setGeometry(QtCore.QRect(50, 410, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_add_column.setFont(font)
        self.Button_add_column.setObjectName("Button_add_column")
        self.Button_read_cell = QtWidgets.QPushButton(self.centralwidget)
        self.Button_read_cell.setGeometry(QtCore.QRect(510, 330, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Button_read_cell.setFont(font)
        self.Button_read_cell.setObjectName("Button_read_cell")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button_add_row.setText(_translate("MainWindow", "add row"))
        self.Button_remove_row.setText(_translate("MainWindow", "remove row"))
        self.Button_remove_column.setText(_translate("MainWindow", "remove column"))
        self.Button_add_column.setText(_translate("MainWindow", "add collumn"))
        self.Button_read_cell.setText(_translate("MainWindow", "Read_cell"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())