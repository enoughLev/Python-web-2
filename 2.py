import sys

from PyQt6.QtCore import QStringListModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel, QPushButton

from forms.form_2_ui import Ui_MainWindow

class DailyPlanner(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.dailyDict = {"Ежедневник начат":"Thu Nov 18 12:43:00 2025"}
        self.model = QStringListModel(self)

        self.enterButton.clicked.connect(self. onEnterButton)

    def onEnterButton(self):
        date = self.dateEdit.dateTime().toString()
        event = self.eventNameLabel.text()
        self.dailyDict[event] = date
        dailyList = list(self.dailyDict.items())
        print(self.dailyDict)
        print(dailyList)
        self.updateListView()

    def updateListView(self): # не знаю как назвать список кроме как list, но он ругается.
        ready_list = []
        for key, value in self.dailyDict.items():
            var = f"{key} - {value}"
            ready_list.append(var)
        #print(ready_list)
        self.model.setStringList(ready_list)
        self.eventList.setModel(self.model)
"""        
        for i in range(0, len(spisok_emae)):
            print(spisok_emae[i])
            self.model.setStringList(spisok_emae[i])
            self.eventList.setModel(self.model)"""



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DailyPlanner()
    ex.show()
    sys.exit(app.exec())