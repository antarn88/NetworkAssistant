from math import log2
from textwrap import wrap

from PySide2.QtCore import Qt, QThread
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QTableWidget, QHeaderView, \
    QTableWidgetItem
from pyperclip import copy

from utilities.PopupWindow import PopupWindow
from utilities.Validator import is_empty, is_correct_network_address, is_correct_number_of_subnets


class IpSubnetCalculation(QWidget):
    def __init__(self):
        super(IpSubnetCalculation, self).__init__()

        # App attributes
        self.calculation_worker = None

        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setAlignment(Qt.AlignTop)
        self.setLayout(main_layout)

        top_bar = QGridLayout()

        # Left, top, right and bottom margins
        top_bar.setContentsMargins(40, 15, 40, 15)
        top_bar.setHorizontalSpacing(40)
        main_layout.addLayout(top_bar)

        starting_network_address_label = QLabel("Kiindulási hálózatcím:")
        number_of_subnets_label = QLabel("Szükséges alhálózatszám:")

        self.starting_network_address_input = QLineEdit()
        self.starting_network_address_input.returnPressed.connect(self.calculation_action)
        self.number_of_subnets_input = QLineEdit()
        self.number_of_subnets_input.returnPressed.connect(self.calculation_action)

        top_bar.addWidget(starting_network_address_label, 0, 0)
        top_bar.addWidget(self.starting_network_address_input, 0, 1)
        top_bar.addWidget(number_of_subnets_label, 1, 0)
        top_bar.addWidget(self.number_of_subnets_input, 1, 1)

        calculation_button = QPushButton("Számítás")
        calculation_button.clicked.connect(self.calculation_action)
        calculation_button.setIcon(QIcon("static/icons/get_info.png"))
        main_layout.addWidget(calculation_button, alignment=Qt.AlignCenter)

        self.table = QTableWidget()
        self.table.itemDoubleClicked.connect(copy_text_action)
        self.table.setColumnCount(6)

        self.table_column_names = ["Hálózatcím",
                                   "IP tartomány",
                                   "Szórási cím",
                                   "Alhálózati maszk",
                                   "Prefix",
                                   "Címezhető host"]

        self.table.setHorizontalHeaderLabels(self.table_column_names)

        # Automatic resizing of the columns to the content
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        # Fixed height of table rows
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        main_layout.addWidget(self.table)

    def calculation_action(self):
        self.calculation_worker = CalculationWorker(self)
        if self.calculation_worker.check_input():
            self.table.setRowCount(0)
            self.calculation_worker.start()


class CalculationWorker(QThread):
    def __init__(self, parent):
        super(CalculationWorker, self).__init__(parent)

        # App attributes
        self.is_first_network = True
        self.network_ip = None
        self.needed_networks = None
        self.default_networkbits = None
        self.subnet_bits = None
        self.prefix = None
        self.first_addressable_ip = None
        self.last_addressable_ip = None
        self.broadcast_ip = None
        self.subnets = []

        self.starting_network_address_input = parent.starting_network_address_input
        self.number_of_subnets_input = parent.number_of_subnets_input
        self.table = parent.table
        self.table_column_names = parent.table_column_names

    def run(self):
        self.generating_subnets()

    def check_input(self):

        # If the starting network address is empty
        if is_empty(self.starting_network_address_input.text()):
            PopupWindow("warning",
                        "A kiindulási hálózatcím nem lehet üres!",
                        self.starting_network_address_input)
            return False
        else:

            # If the starting network address is incorrect
            if not is_correct_network_address(self.starting_network_address_input.text()):
                PopupWindow("warning",
                            "Érvénytelen a kiindulási hálózatcím! Ellenőrizd!",
                            self.starting_network_address_input)
                return False

        # If number of subnets is empty
        if is_empty(self.number_of_subnets_input.text()):
            PopupWindow("warning",
                        "Add meg, hogy hány alhálózatot szeretnél!",
                        self.number_of_subnets_input)
            return False
        else:

            # If number of subnets is incorrect
            if not is_correct_number_of_subnets(self.number_of_subnets_input.text()):
                PopupWindow("warning",
                            "Érvénytelen az alhálózatszám megadása! Ellenőrizd!",
                            self.number_of_subnets_input)
                return False

        self.storing_input_data()

        # If max addressable host least two and have least one needed network
        if self.get_max_addressable_hosts() >= 2 and int(self.needed_networks) >= 1:
            return True
        else:

            # Unreal subnet number
            PopupWindow("warning",
                        "Ennyi alhálózatot nem lehet legenerálni a megadott hálózati címhez!",
                        self.number_of_subnets_input)
            return False

    def storing_input_data(self):
        self.network_ip = self.starting_network_address_input.text()
        self.needed_networks = self.number_of_subnets_input.text()
        self.subnet_bits = int(log2(int(power_bit_length(int(self.needed_networks)))))

    def get_starting_network_default_mask(self):
        first_octet = int(self.network_ip.split(".")[0])

        if 1 <= first_octet < 128:
            return "255.0.0.0"
        elif 128 <= first_octet < 192:
            return "255.255.0.0"
        elif 192 <= first_octet < 224:
            return "255.255.255.0"

    def get_mask(self):
        mask_32bit = ((self.default_networkbits + self.subnet_bits) * "1").ljust(32, "0")
        self.prefix = mask_32bit.count("1")
        return get_ip_from_32bit_format(mask_32bit)

    def set_network_ip(self):
        if self.is_first_network:
            return self.network_ip
        else:
            next_network_ip_32bit = bin(int(get_32bit_format(self.broadcast_ip), 2) +
                                        int("1", 2)).replace("0b", "").rjust(32, "0")
            self.network_ip = get_ip_from_32bit_format(next_network_ip_32bit)

    def set_first_addressable_ip(self):
        first_addressable_ip_32bit = bin(int(get_32bit_format(self.network_ip), 2) +
                                         int("1", 2)).replace("0b", "").rjust(32, "0")
        self.first_addressable_ip = get_ip_from_32bit_format(first_addressable_ip_32bit)

    def set_last_addressable_ip(self):
        bin1 = int(get_32bit_format(self.network_ip), 2)
        bin2 = int(bin(self.get_max_addressable_hosts()).replace("0b", ""), 2)
        last_addressable_ip_32bit = bin(bin1 + bin2).replace("0b", "").rjust(32, "0")
        self.last_addressable_ip = get_ip_from_32bit_format(last_addressable_ip_32bit)

    def set_broadcast_ip(self):
        broadcast_ip_32bit = bin(int(get_32bit_format(self.last_addressable_ip), 2) +
                                 int("1", 2)).replace("0b", "").rjust(32, "0")
        self.broadcast_ip = get_ip_from_32bit_format(broadcast_ip_32bit)

    def get_max_addressable_hosts(self):
        self.default_networkbits = 32 - get_32bit_format(self.get_starting_network_default_mask()).count("0")
        return pow(2, ((self.default_networkbits + self.subnet_bits) * "1").ljust(32, "0").count("0")) - 2

    def inject_data_to_dict(self):
        self.subnets.append({self.table_column_names[0]: self.network_ip,
                             self.table_column_names[1]: f"{self.first_addressable_ip} - "
                                                         f"{self.last_addressable_ip}",
                             self.table_column_names[2]: self.broadcast_ip,
                             self.table_column_names[3]: self.get_mask(),
                             self.table_column_names[4]: f"/{self.prefix}",
                             self.table_column_names[5]: self.get_max_addressable_hosts()})

    def inject_data_to_table(self):
        row = 0
        for subnet in self.subnets:
            self.table.insertRow(row)
            column = 0
            for i in subnet.items():
                value = str(i[1])
                item = QTableWidgetItem()
                item.setText(value)
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(row, column, item)
                column += 1
            row += 1

    def generating_subnets(self):
        self.table.setRowCount(0)
        for subnet in range(int(self.needed_networks)):
            self.set_network_ip()
            self.set_first_addressable_ip()
            self.set_last_addressable_ip()
            self.set_broadcast_ip()
            self.inject_data_to_dict()
            self.is_first_network = False
        self.inject_data_to_table()


# Copying content of cell to clipboard
def copy_text_action(item):
    copy(item.text())


# A function that converts the entered number to the nearest 2 powers
def power_bit_length(x):
    return 2 ** (x - 1).bit_length()


# Returns a 32 bit format from an IP address
def get_32bit_format(ip_address):
    format_32bit = ""
    for octet in ip_address.split("."):
        format_32bit += f'{bin(int(octet)).replace("0b", "").rjust(8, "0")}'
    return format_32bit


# Returns a decimal IP address from a 32 bit format
def get_ip_from_32bit_format(format_32bit):
    ip_dec = ""
    for octet in wrap(format_32bit, 8):
        ip_dec += f"{int(octet, 2)}."
    return ip_dec[:-1]
