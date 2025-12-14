import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from forms.form_3_ui import Ui_MainWindow


class NotebookApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Записная книжка")

        self.add_button.clicked.connect(self.add_contact)

        self.clear_button.clicked.connect(self.clear_list)


    def add_contact(self):
        name = self.name_edit.text().strip()
        phone = self.phone_edit.text().strip()

        if name and phone:
            print(f"{name}, {phone}")
            contact = f"{name}: {phone}"
            self.contact_list.addItem(contact)
            self.name_edit.clear()
            self.phone_edit.clear()
            self.name_edit.setFocus()
        else:
            print("Field Name or Phone is empty")


    def clear_list(self):
        self.contact_list.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NotebookApp()
    ex.show()
    sys.exit(app.exec())
