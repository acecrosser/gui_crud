import sys
from PySide6 import QtWidgets
from ui.mainWindow import Ui_MainWindow
from ui.secondWindow import Ui_Form
from Form import Form
from GuiCrudMaker import GuiCrudMaker


class WishListCrud(QtWidgets.QMainWindow, Ui_MainWindow):

    # data = GuiCrudMaker()
    # item = data.read()
    # col = QTableWidgetItem(item)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(open_second_window)
        list_item = maker_list()
        for i in list_item:
            self.listWidget.addItem(i)
        self.listWidget.clicked.connect(open_second_window)


def maker_list():
    data = GuiCrudMaker()
    item = data.read()
    list_item = []
    for k, i in enumerate(item, 1):
        list_item.append(f'{k} - {i[1]} - {i[2]} - {i[3]} - {i[4]}')
    return list_item


def open_second_window():
    form = QtWidgets.QDialog()
    ui = Form()
    ui.setupUi(form)
    form.show()

    def closed_window():
        form.close()

    ui.cancelButton.clicked.connect(closed_window)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wsl = WishListCrud()
    wsl.show()
    sys.exit(app.exec_())


