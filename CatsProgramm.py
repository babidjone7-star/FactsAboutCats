from PySide6.QtWidgets import QApplication, QDialog
from cats import Ui_Dialog
import sys
import requests

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.GenerateFact.clicked.connect(self.gener)
    def gener(self):
        try:
         self.responce = requests.get("https://catfact.ninja/fact")
         self.data = self.responce.json()
         self.fact = self.data["fact"]
         self.ui.FactAboutCats .setText(self.fact)
        except Exception as e:
           self.ui.FactAboutCats.setText("Плохое соединение с интеренетом")
           return
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())