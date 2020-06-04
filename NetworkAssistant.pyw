from sys import argv

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QTabWidget

from modules.IpInformation import IpInformation
from modules.IpSubnetCalculation import IpSubnetCalculation
from modules.NumberConversion import NumberConversion
from modules.VlsmCalculation import VlsmCalculation
from utilities.Style import style


class NetworkAssistant(QMainWindow):
    def __init__(self):
        super(NetworkAssistant, self).__init__()

        # The size of the starting window
        self.resize(950, 600)

        # The version of the program
        version = "1.0.4"

        # The title of the program
        self.setWindowTitle(f"Hálózati Segéd {version}")

        # The icon of the program
        self.setWindowIcon(QIcon("static/icons/main_icon.png"))

        # Before using the main layout, need to create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        tabwidget = QTabWidget()
        tabwidget.addTab(IpInformation(), "IP információk")
        tabwidget.addTab(NumberConversion(), "Számátváltás")
        tabwidget.addTab(IpSubnetCalculation(), "Azonos méretű alhálózatokra bontás")
        tabwidget.addTab(VlsmCalculation(), "VLSM számítás")
        main_layout.addWidget(tabwidget)

        # Set stylesheet
        self.setStyleSheet(style())


if __name__ == '__main__':
    app = QApplication(argv)
    win = NetworkAssistant()
    win.show()
    app.exec_()
