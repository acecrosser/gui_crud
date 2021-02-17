import sys
from PySide6 import QtWidgets
from ui.mainWindow import Ui_MainWindow
from GuiCrudMaker import GuiCrudMaker


class WishListCrud(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.create_wish)
        self.list_item = maker_list()
        self.wish_list()
        # self.listWidget.clicked.connect()

    def wish_list(self):
        self.listWidget.clear()
        for i in self.list_item:
            self.listWidget.addItem(i)

    def create_wish(self):
        print('Мы тут')
        title = self.titleEdit.text()
        price = self.priceBox.text()
        link = self.linkEdit.text()
        text = self.textEdit.text()

        data = []
        data.append(title)
        data.append(price)
        data.append(link)
        data.append(text)

        db = GuiCrudMaker()
        db.create(tuple(data))
        maker_list()
        self.wish_list()


def maker_list():
    data = GuiCrudMaker()
    item = data.read()
    list_item = []
    for k, i in enumerate(item, 1):
        list_item.append(f'{k} - {i[1]} - {i[2]} - {i[3]} - {i[4]}')
    return list_item


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    wsl = WishListCrud()
    wsl.show()
    sys.exit(app.exec_())


