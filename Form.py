import sys
from ui.secondWindow import Ui_Form
from PySide6 import QtWidgets
from GuiCrudMaker import GuiCrudMaker


class Form(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.saveButton.clicked.connect(self.create_wish)
        self.cancelButton.clicked.connect(self.close)

    def create_wish(self):
        print('Мы тут')
        title = self.titleLine.text()
        price = self.priceLine.text()
        link = self.linkLine.text()
        text = self.textArea.text()

        print(self.title)
        data = tuple(title + price + link + text)
        print(data)


def open_window():
    global form
    form = QtWidgets.QWidget()
    ui = Form()
    ui.setupUi(form)
    form.show()
