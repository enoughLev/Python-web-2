import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel, QPushButton

from form_1_ui import Ui_MainWindow

class DrawFlag(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 600)

        self.flag = [0, 0, 0]
        self.colors = ["", "Красный", "Белый", "Синий"]

        self.SecondChoose.buttonClicked.connect(self.clicked_on_group_2)
        self.ThirdChoose.buttonClicked.connect(self.clicked_on_group_3)
        self.drawButton.clicked.connect(self.draw)


    def draw(self):
        self.label.setText(self.colors[self.flag[0]])
        self.label_2.setText(self.colors[self.flag[1]])
        self.label_3.setText(self.colors[self.flag[2]])


    def clicked_on_group_1(self, button):
        id_1 = self.FirstChoose.id(button)
        self.flag[0] = id_1
        print(self.flag)

    def clicked_on_group_2(self, button):
        id_2 = self.SecondChoose.id(button)
        self.flag[1] = id_2
        print(self.flag)

    def clicked_on_group_3(self, button):
        id_3 = self.ThirdChoose.id(button)
        self.flag[2] = id_3
        print(self.flag)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawFlag()
    ex.show()
    sys.exit(app.exec())