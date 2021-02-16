from ui.secondWindow import Ui_Form
from PySide6 import QtWidgets
from GuiCrudMaker import GuiCrudMaker


class Form(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.saveButton.clicked.connect(self.create_wish)

    def create_wish(self):
        title = self.titleLine.text()
        price = self.priceLine.text()
        link = self.linkLine.text()
        text = self.textArea.text()

        data = tuple(title + price + link + text)
        print(data)
