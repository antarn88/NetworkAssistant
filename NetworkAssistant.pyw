from sys import argv

from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QTabWidget, QAction

from modules.IpInformation import IpInformation
from modules.IpSubnetCalculation import IpSubnetCalculation
from modules.NumberConversion import NumberConversion
from modules.VlsmCalculation import VlsmCalculation
from utilities.ManageLng import ManageLng
from utilities.Style import style


class NetworkAssistant(QMainWindow):
    def __init__(self):
        super(NetworkAssistant, self).__init__()

        # Use language settings
        self.ml = ManageLng()

        # The size of the starting window
        self.resize(950, 600)

        # The version of the program
        self.version = "v1.1"

        # The title of the program
        self.setWindowTitle(f"{self.ml.get_tr_text('main_app_title')} {self.version}")

        # The icon of the program
        self.setWindowIcon(QIcon("static/images/main_icon.png"))

        # Menu
        menu = self.menuBar()

        self.languages_menu = menu.addMenu(self.ml.get_tr_text("menubar_lang"))

        self.set_english_lng_action = QAction(QIcon("static/images/english_icon.png"),
                                              self.ml.get_tr_text("menubar_lang_eng"), self.languages_menu)
        self.set_english_lng_action.triggered.connect(self.set_english_lng)
        self.languages_menu.addAction(self.set_english_lng_action)

        self.set_hungarian_lng_action = QAction(QIcon("static/images/hungarian_icon.png"),
                                                self.ml.get_tr_text("menubar_lang_hun"), self.languages_menu)
        self.set_hungarian_lng_action.triggered.connect(self.set_hungarian_lng)
        self.languages_menu.addAction(self.set_hungarian_lng_action)

        # Before using the main layout, need to create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.ip_information = IpInformation()
        self.number_conversion = NumberConversion()
        self.ip_subnet_calculation = IpSubnetCalculation()
        self.vlsm_calculation = VlsmCalculation()

        self.tabwidget = QTabWidget()
        self.tabwidget.addTab(self.ip_information, self.ml.get_tr_text("tab_ip_information"))
        self.tabwidget.addTab(self.number_conversion, self.ml.get_tr_text("tab_number_conversion"))
        self.tabwidget.addTab(self.ip_subnet_calculation, self.ml.get_tr_text("tab_ip_subnet_calculation"))
        self.tabwidget.addTab(self.vlsm_calculation, self.ml.get_tr_text("tab_vlsm_calculation"))
        main_layout.addWidget(self.tabwidget)

        # Set stylesheet
        self.setStyleSheet(style())

    def set_hungarian_lng(self):
        lang = "Hungarian"
        self.ml = ManageLng(lang)

        self.setWindowTitle(f"{self.ml.get_tr_text('main_app_title')} {self.version}")
        self.languages_menu.setTitle(self.ml.get_tr_text("menubar_lang"))
        self.set_english_lng_action.setText(self.ml.get_tr_text("menubar_lang_eng"))
        self.set_hungarian_lng_action.setText(self.ml.get_tr_text("menubar_lang_hun"))
        self.tabwidget.setTabText(0, self.ml.get_tr_text("tab_ip_information"))
        self.tabwidget.setTabText(1, self.ml.get_tr_text("tab_number_conversion"))
        self.tabwidget.setTabText(2, self.ml.get_tr_text("tab_ip_subnet_calculation"))
        self.tabwidget.setTabText(3, self.ml.get_tr_text("tab_vlsm_calculation"))
        self.re_translate_tabs(lang)

    def set_english_lng(self):
        lang = "English"
        self.ml = ManageLng(lang)

        self.setWindowTitle(f"{self.ml.get_tr_text('main_app_title')} {self.version}")
        self.languages_menu.setTitle(self.ml.get_tr_text("menubar_lang"))
        self.set_english_lng_action.setText(self.ml.get_tr_text("menubar_lang_eng"))
        self.set_hungarian_lng_action.setText(self.ml.get_tr_text("menubar_lang_hun"))
        self.tabwidget.setTabText(0, self.ml.get_tr_text("tab_ip_information"))
        self.tabwidget.setTabText(1, self.ml.get_tr_text("tab_number_conversion"))
        self.tabwidget.setTabText(2, self.ml.get_tr_text("tab_ip_subnet_calculation"))
        self.tabwidget.setTabText(3, self.ml.get_tr_text("tab_vlsm_calculation"))
        self.re_translate_tabs(lang)

    def re_translate_tabs(self, lang):
        self.ip_information.re_translate_ui(lang)
        self.number_conversion.re_translate_ui(lang)
        self.ip_subnet_calculation.re_translate_ui(lang)
        self.vlsm_calculation.re_translate_ui(lang)


if __name__ == '__main__':
    app = QApplication(argv)
    win = NetworkAssistant()
    win.show()
    app.exec_()
