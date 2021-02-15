import sys
from PySide6 import QtWidgets
from ui.mainWindow import Ui_MainWindow
from ui.secondWindow import Ui_Form


class WishListCrud(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wsl = WishListCrud()
    wsl.show()
    sys.exit(app.exec_())


