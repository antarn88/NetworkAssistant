from math import log2
from textwrap import wrap

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QWidget, QTableWidget, QLabel, QPushButton, QGridLayout, QLineEdit, QTableWidgetItem, \
    QHeaderView
from pyperclip import copy

from utilities.PopupWindow import PopupWindow
from utilities.Validator import is_empty, is_correct_network_address, is_correct_endpoint_numbers_per_network, is_correct_prefix


class VlsmCalculation(QWidget):
    def __init__(self):
        super(VlsmCalculation, self).__init__()

        # App attributes
        self.network_ip = None
        self.prefix = None
        self.network_hosts = None
        self.length_of_subnets = []
        self.subnets = []

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
        endpoint_numbers_per_network_label = QLabel("Végpontszámok a hálózatokban (vesszővel válaszd el őket!):")
        starting_network_prefix_label = QLabel("Kiindulási hálózat prefixe (opcionális):")

        self.starting_network_address_input = QLineEdit()
        self.starting_network_address_input.returnPressed.connect(self.calculation_action)

        self.starting_network_prefix_input = QLineEdit()
        self.starting_network_prefix_input.returnPressed.connect(self.calculation_action)

        self.endpoint_numbers_per_network_input = QLineEdit()
        self.endpoint_numbers_per_network_input.returnPressed.connect(self.calculation_action)

        top_bar.addWidget(starting_network_address_label, 0, 0)
        top_bar.addWidget(self.starting_network_address_input, 0, 1)

        top_bar.addWidget(starting_network_prefix_label, 1, 0)
        top_bar.addWidget(self.starting_network_prefix_input, 1, 1)

        top_bar.addWidget(endpoint_numbers_per_network_label, 2, 0)
        top_bar.addWidget(self.endpoint_numbers_per_network_input, 2, 1)

        calculation_button = QPushButton("Számítás")
        calculation_button.setIcon(QIcon("static/icons/get_info.png"))
        calculation_button.clicked.connect(self.calculation_action)
        main_layout.addWidget(calculation_button, alignment=Qt.AlignCenter)

        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.itemDoubleClicked.connect(copy_text_action)

        # Set table header labels
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

        # If endpoint numbers are empty
        if is_empty(self.endpoint_numbers_per_network_input.text()):
            PopupWindow("warning",
                        "Add meg, hogy hány gépszámú hálózatokat szeretnél!",
                        self.endpoint_numbers_per_network_input)
            return False
        else:

            # If endpoint numbers are incorrect
            if not is_correct_endpoint_numbers_per_network(self.endpoint_numbers_per_network_input.text()):
                PopupWindow("warning",
                            "Érvénytelen a gépszámok megadása! Ellenőrizd!",
                            self.endpoint_numbers_per_network_input)
                return False

        # If prefix is incorrect
        self.prefix = self.starting_network_prefix_input.text().replace("/", "").replace("\\", "")
        if not is_correct_prefix(self.prefix):
            PopupWindow("warning",
                        "Érvénytelen a kiindulási hálózat prefixe! Ellenőrizd!",
                        self.starting_network_prefix_input)
            return False
        return True

    def inject_data_to_table(self):
        row = 0
        for subnet in self.subnets:
            self.table.insertRow(row)
            column = 0
            for i in subnet.items():
                value = str(i[1])
                self.table.setItem(row, column, TableItem(value))
                column += 1
            row += 1

    def storing_input_data(self):
        self.network_ip = self.starting_network_address_input.text()
        self.network_hosts = self.endpoint_numbers_per_network_input.text()

    def calculation_action(self):
        if self.check_input():
            # Stores user-specified data
            self.storing_input_data()

            # Resets table before injects data
            self.table.setRowCount(0)

            self.processing()
            self.inject_data_to_table()

            # Clears lists to next calculation
            self.length_of_subnets.clear()
            self.subnets.clear()

    def inject_data_to_dict(self):
        for network in self.length_of_subnets:
            hostbits = int(log2(network))
            prefix = 32 - hostbits
            mask = get_ip_from_32bit_format(("0" * hostbits).rjust(32, "1"))

            self.subnets.append({self.table_column_names[0]: self.network_ip,
                                 self.table_column_names[1]: f"{get_first_addressable_ip(self.network_ip)} - "
                                                             f"{get_last_addressable_ip(self.network_ip, mask)}",
                                 self.table_column_names[2]: get_broadcast_ip(self.network_ip, mask),
                                 self.table_column_names[3]: mask,
                                 self.table_column_names[4]: f"/{prefix}",
                                 self.table_column_names[5]: pow(2, hostbits) - 2})

            self.network_ip = get_next_network_ip(self.network_ip, mask)

    def processing(self):

        # User-specified hosts are converted to the nearest 2 powers
        for hosts in self.network_hosts.split(","):
            if int(hosts) > 0:
                hosts = int(hosts) + 2
                self.length_of_subnets.append(power_bit_length(int(hosts)))

        # The largest host network will be pre-sorting
        self.length_of_subnets.sort(reverse=True)
        sum_all_hosts = sum(self.length_of_subnets)

        if is_empty(self.prefix):
            first_octet = int(self.network_ip.split(".")[0])

            # Determining what could be the default mask based on network address
            if 1 <= first_octet < 128:
                if sum_all_hosts <= pow(2, 24):
                    self.inject_data_to_dict()
                else:
                    PopupWindow("warning",
                                "Irreálisan sok állomást szeretnél!\n"
                                "Ellenőrizd az adatokat!",
                                self.endpoint_numbers_per_network_input)

            elif 128 <= first_octet < 192:
                if sum_all_hosts <= pow(2, 16):
                    self.inject_data_to_dict()
                else:
                    PopupWindow("warning",
                                "Túl sok állomást szeretnél egy 'B' osztályú /16 főhálózathoz képest!\n"
                                "Próbálkozz inkább egy 'A' osztályú kiindulási hálózattal, vagy egy\nkisebb prefix-szel!",
                                self.endpoint_numbers_per_network_input)

            elif 192 <= first_octet < 224:
                if sum_all_hosts <= pow(2, 8):
                    self.inject_data_to_dict()
                else:
                    PopupWindow("warning",
                                "Túl sok állomást szeretnél egy 'C' osztályú /24 főhálózathoz képest!\n"
                                "Próbálkozz inkább egy 'B' vagy egy 'A' osztályú kiindulási hálózattal, esetleg kisebb prefix-szel!",
                                self.endpoint_numbers_per_network_input)
        else:
            if sum_all_hosts <= pow(2, 32 - int(self.prefix)):
                self.inject_data_to_dict()
            else:
                PopupWindow("warning",
                            f"Túl sok állomást szeretnél egy /{self.prefix} főhálózathoz képest!\n"
                            f"Ellenőrizd az adatokat!",
                            self.endpoint_numbers_per_network_input)


class TableItem(QTableWidgetItem):
    def __init__(self, text):
        super(TableItem, self).__init__(text)
        self.setText(text)
        self.setTextAlignment(Qt.AlignCenter)
        self.setFlags(Qt.ItemIsEnabled)


# Copying content of cell to clipboard
def copy_text_action(item):
    copy(item.text())


# A function that converts the entered number to the nearest 2 powers
def power_bit_length(x):
    return 2 ** (x - 1).bit_length()


def get_mask_from_prefix(prefix):
    subnet_mask_dec = ""
    for octet in wrap(("0" * (32 - prefix)).rjust(32, "1"), 8):
        subnet_mask_dec += f"{int(octet, 2)}."
    return subnet_mask_dec[:-1]


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


def get_first_addressable_ip(network_ip):
    first_addressable_ip_bin_32bit = bin(int(get_32bit_format(network_ip), 2) +
                                         int("1", 2)).replace("0b", "").rjust(32, "0")
    return get_ip_from_32bit_format(first_addressable_ip_bin_32bit)


def get_last_addressable_ip(network_ip, mask):
    broadcast_ip_32bit = get_32bit_format(get_broadcast_ip(network_ip, mask))
    last_addressable_ip_bin_32bit = bin(int(broadcast_ip_32bit, 2) -
                                        int("1", 2)).replace("0b", "").rjust(32, "0")
    return get_ip_from_32bit_format(last_addressable_ip_bin_32bit)


def get_broadcast_ip(network_ip, mask):
    broadcast_ip_32bit = f"{get_32bit_format(network_ip)[:-get_32bit_format(mask).count('0')]}" \
                         f"{'1' * get_32bit_format(mask).count('0')}"
    return get_ip_from_32bit_format(broadcast_ip_32bit)


def get_next_network_ip(network_ip, mask):
    broadcast_ip_32bit = get_32bit_format(get_broadcast_ip(network_ip, mask))
    next_network_ip_32bit = bin(int(broadcast_ip_32bit, 2) +
                                int("1", 2)).replace("0b", "").rjust(32, "0")
    return get_ip_from_32bit_format(next_network_ip_32bit)
