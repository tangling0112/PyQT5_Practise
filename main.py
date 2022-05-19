from PyQt5.QtWidgets import QMainWindow, QApplication
from Designer.untitled import Ui_MainWindow
import sys

app = QApplication(sys.argv)
MainWindow = QMainWindow()
Ui = Ui_MainWindow()
Ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
