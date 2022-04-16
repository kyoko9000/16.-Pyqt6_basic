# **************************man hinh loai 2*************************
import sys
# pip install pyqt5
from PyQt6.QtWidgets import QApplication, QMainWindow, QFontDialog, QColorDialog
from gui1 import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.pushButton.clicked.connect(self.openFontDialog)
        self.uic.pushButton_2.clicked.connect(self.change_color_text)
        self.uic.pushButton_3.clicked.connect(self.change_color_background)

    def openFontDialog(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.uic.label.setFont(font)
            print(font.toString())

    def change_color_text(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.uic.comboBox.setStyleSheet("color: " + color.name())
            print(color.name())

    def change_color_background(self):
        # self.uic.label.setStyleSheet("background-color:" + "#ff0000" + ";" + "color: " + "#ffff00")
        color = QColorDialog.getColor()
        if color.isValid():
            self.uic.label.setStyleSheet("background-color:" + color.name())
            print(color.name())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
