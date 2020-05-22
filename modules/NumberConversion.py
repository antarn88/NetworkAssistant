from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QVBoxLayout, QWidget, QLabel, QGroupBox, QLineEdit, QGridLayout, QRadioButton, QPushButton
from pyperclip import copy

from utilities.PopupWindow import PopupWindow
from utilities.Validator import is_empty, is_correct_binary, is_correct_decimal, is_correct_hexadecimal, is_correct_any_ip_dec, \
    is_correct_any_ip_bin


class NumberConversion(QWidget):
    def __init__(self):
        super(NumberConversion, self).__init__()

        main_layout = QGridLayout()
        self.setLayout(main_layout)

        # Input
        inputbox = QGroupBox("Bemenet")
        inputbox.setMaximumWidth(400)

        main_layout.addWidget(inputbox, 0, 0)

        inputbox_layout = QGridLayout()
        inputbox_layout.setHorizontalSpacing(25)
        inputbox_layout.setVerticalSpacing(35)
        inputbox_layout.setAlignment(Qt.AlignCenter)

        inputbox.setLayout(inputbox_layout)

        input_number_label = QLabel("Bemeneti szám:")
        self.input_number_textfield = QLineEdit()
        self.input_number_textfield.setPlaceholderText("192")
        self.input_number_textfield.setAlignment(Qt.AlignCenter)
        self.input_number_textfield.returnPressed.connect(self.convert_action)

        inputbox_layout.addWidget(input_number_label, 0, 0, alignment=Qt.AlignCenter)
        inputbox_layout.addWidget(self.input_number_textfield, 0, 1)

        button_layout = QVBoxLayout()
        self.bin_button = QRadioButton("Bináris")
        self.bin_button.clicked.connect(lambda: self.input_number_textfield.setPlaceholderText("11100010"))
        self.dec_button = QRadioButton("Decimális")
        self.dec_button.clicked.connect(lambda: self.input_number_textfield.setPlaceholderText("192"))
        hex_button = QRadioButton("Hexadecimális")
        hex_button.clicked.connect(lambda: self.input_number_textfield.setPlaceholderText("FF"))
        self.dec_button.setChecked(True)
        button_layout.addWidget(self.bin_button)
        button_layout.addWidget(self.dec_button)
        button_layout.addWidget(hex_button)
        inputbox_layout.addLayout(button_layout, 0, 3, 1, 2)

        convert_button = QPushButton("Átváltás")
        convert_button.clicked.connect(self.convert_action)
        convert_button.setIcon(QIcon("static/icons/exchange.png"))
        inputbox_layout.addWidget(convert_button, 1, 1, alignment=Qt.AlignCenter)

        # Output
        outputbox = QGroupBox("Kimenet")
        main_layout.addWidget(outputbox, 0, 1)
        outputbox_layout = QGridLayout()
        outputbox_layout.setHorizontalSpacing(25)
        outputbox.setLayout(outputbox_layout)

        bin_label = QLabel("Bináris:")
        bin_label.setAlignment(Qt.AlignCenter)

        dec_label = QLabel("Decimális:")
        dec_label.setAlignment(Qt.AlignCenter)

        hex_label = QLabel("Hexadecimális:")
        hex_label.setAlignment(Qt.AlignCenter)

        self.bin_output = QLineEdit()
        self.bin_output.setReadOnly(True)
        self.bin_output.setAlignment(Qt.AlignCenter)

        self.dec_output = QLineEdit()
        self.dec_output.setReadOnly(True)
        self.dec_output.setAlignment(Qt.AlignCenter)

        self.hex_output = QLineEdit()
        self.hex_output.setReadOnly(True)
        self.hex_output.setAlignment(Qt.AlignCenter)

        bin_output_copy_button = QPushButton("Másolás")
        bin_output_copy_button.setIcon(QIcon("static/icons/copy_clipboard.png"))
        bin_output_copy_button.clicked.connect(lambda: copy_action(self.bin_output.text()))

        dec_output_copy_button = QPushButton("Másolás")
        dec_output_copy_button.setIcon(QIcon("static/icons/copy_clipboard.png"))
        dec_output_copy_button.clicked.connect(lambda: copy_action(self.dec_output.text()))

        hex_output_copy_button = QPushButton("Másolás")
        hex_output_copy_button.setIcon(QIcon("static/icons/copy_clipboard.png"))
        hex_output_copy_button.clicked.connect(lambda: copy_action(self.hex_output.text()))

        outputbox_layout.addWidget(bin_label, 0, 0)
        outputbox_layout.addWidget(self.bin_output, 0, 1)
        outputbox_layout.addWidget(bin_output_copy_button, 0, 2)

        outputbox_layout.addWidget(dec_label, 1, 0)
        outputbox_layout.addWidget(self.dec_output, 1, 1)
        outputbox_layout.addWidget(dec_output_copy_button, 1, 2)

        outputbox_layout.addWidget(hex_label, 2, 0)
        outputbox_layout.addWidget(self.hex_output, 2, 1)
        outputbox_layout.addWidget(hex_output_copy_button, 2, 2)

        # IP address/mask number conversion
        ip_address_number_conversion_box = QGroupBox("IP cím/maszk számátváltás")
        main_layout.addWidget(ip_address_number_conversion_box, 1, 0, 1, 2)

        ip_address_number_conversion_layout = QGridLayout()
        ip_address_number_conversion_layout.setAlignment(Qt.AlignCenter)
        ip_address_number_conversion_layout.setHorizontalSpacing(25)
        ip_address_number_conversion_layout.setVerticalSpacing(24)
        ip_address_number_conversion_box.setLayout(ip_address_number_conversion_layout)

        input_label = QLabel("Bemeneti IP cím/maszk:")
        input_label.setAlignment(Qt.AlignCenter)
        input_label.setMaximumWidth(150)
        self.input_textfield = QLineEdit()
        self.input_textfield.setPlaceholderText("192.168.1.1")
        self.input_textfield.setAlignment(Qt.AlignLeft)
        self.input_textfield.setMaximumWidth(300)
        self.input_textfield.setAlignment(Qt.AlignCenter)
        self.input_textfield.returnPressed.connect(self.convert_action_2)
        ip_address_number_conversion_layout.addWidget(input_label, 0, 0)
        ip_address_number_conversion_layout.addWidget(self.input_textfield, 0, 1)

        button_layout_2 = QVBoxLayout()
        self.dec_to_bin_button = QRadioButton("Decimálisból binárisba")
        self.dec_to_bin_button.clicked.connect(lambda: self.input_textfield.setPlaceholderText("192.168.1.1"))
        self.dec_to_bin_button.setMaximumWidth(150)

        bin_to_dec_button = QRadioButton("Binárisból decimálisba")
        bin_to_dec_button.clicked.connect(lambda: self.input_textfield.setPlaceholderText("11000000.10101000.00000001.00000001"))
        bin_to_dec_button.setMaximumWidth(150)
        self.dec_to_bin_button.setChecked(True)
        button_layout_2.addWidget(self.dec_to_bin_button)
        button_layout_2.addWidget(bin_to_dec_button)
        ip_address_number_conversion_layout.addLayout(button_layout_2, 0, 2)

        output_label = QLabel("Kimeneti IP cím/maszk:")
        output_label.setAlignment(Qt.AlignCenter)
        self.output_textfield = QLineEdit()
        self.output_textfield.setMaximumWidth(300)
        self.output_textfield.setReadOnly(True)
        self.output_textfield.setAlignment(Qt.AlignCenter)
        ip_address_number_conversion_layout.addWidget(output_label, 1, 0)
        ip_address_number_conversion_layout.addWidget(self.output_textfield, 1, 1)

        output_textfield_copy_button = QPushButton("Másolás")
        output_textfield_copy_button.setIcon(QIcon("static/icons/copy_clipboard.png"))
        output_textfield_copy_button.clicked.connect(lambda: copy_action(self.output_textfield.text()))
        ip_address_number_conversion_layout.addWidget(output_textfield_copy_button, 1, 2, alignment=Qt.AlignLeft)

        convert_button_2 = QPushButton("Átváltás")
        convert_button_2.clicked.connect(self.convert_action_2)
        convert_button_2.setIcon(QIcon("static/icons/exchange.png"))
        ip_address_number_conversion_layout.addWidget(convert_button_2, 2, 0, 1, 3, alignment=Qt.AlignHCenter)

    def convert_action(self):
        if is_empty(self.input_number_textfield.text()):
            PopupWindow("warning",
                        "A számátváltáshoz töltsd ki a bemeneti szám mezőt!",
                        self.input_number_textfield)
        else:
            if self.bin_button.isChecked():
                self.source_bin(self.input_number_textfield.text())
            elif self.dec_button.isChecked():
                self.source_dec(self.input_number_textfield.text())
            else:
                self.source_hex(self.input_number_textfield.text())

    def source_bin(self, bin_number):
        bin_number_corrected = get_corrected_number(bin_number)
        bin_number_corrected_byte = bin_number_corrected.rjust(8, "0")
        if not is_correct_binary(bin_number_corrected):
            PopupWindow("warning",
                        "Hibás bináris szám! Ellenőrizd!",
                        self.input_number_textfield)
        else:
            if 0 <= int(bin_number_corrected, 2) <= 255:
                if bin_number_corrected != bin_number_corrected_byte:
                    bin_format = f"{bin_number_corrected} (byte formában: {bin_number_corrected_byte})"
                else:
                    bin_format = bin_number_corrected
            else:
                bin_format = bin_number_corrected
            dec_format = str(int(bin_number_corrected, 2))
            hex_format = hex(int(bin_number_corrected, 2)).replace("0x", "").upper()
            self.bin_output.setText(bin_format)
            self.dec_output.setText(dec_format)
            self.hex_output.setText(hex_format)

    def source_dec(self, dec_number):
        dec_number_corrected = get_corrected_number(dec_number)
        if not is_correct_decimal(dec_number_corrected):
            PopupWindow("warning",
                        "Hibás decimális szám! Ellenőrizd!",
                        self.input_number_textfield)
        else:
            if 0 <= int(dec_number_corrected) <= 255:
                bin_format_base = bin(int(dec_number_corrected)).replace("0b", "")
                bin_format_base_byte = bin_format_base.rjust(8, "0")
                if bin_format_base != bin_format_base_byte:
                    bin_format = f"{bin_format_base} (byte formában: {bin_format_base_byte})"
                else:
                    bin_format = bin_format_base
            else:
                bin_format = bin(int(dec_number_corrected)).replace("0b", "")
            dec_format = dec_number_corrected
            hex_format = hex(int(dec_number_corrected)).replace("0x", "").upper()
            self.bin_output.setText(bin_format)
            self.dec_output.setText(dec_format)
            self.hex_output.setText(hex_format)

    def source_hex(self, hex_number):
        hex_number_corrected = get_corrected_number(hex_number).upper()
        if not is_correct_hexadecimal(hex_number_corrected):
            PopupWindow("warning",
                        "Hibás hexadecimális szám! Ellenőrizd!",
                        self.input_number_textfield)
        else:
            if 0 <= int(hex_number_corrected, 16) <= 255:
                bin_format_base = bin(int(hex_number_corrected, 16)).replace("0b", "")
                bin_format_base_byte = bin_format_base.rjust(8, "0")
                if bin_format_base != bin_format_base_byte:
                    bin_format = f"{bin_format_base} (byte formában: {bin_format_base_byte})"
                else:
                    bin_format = bin_format_base
            else:
                bin_format = bin(int(hex_number_corrected, 16)).replace("0b", "")
            dec_format = str(int(hex_number_corrected, 16))
            hex_format = hex_number_corrected
            self.bin_output.setText(bin_format)
            self.dec_output.setText(dec_format)
            self.hex_output.setText(hex_format)

    def convert_action_2(self):
        if is_empty(self.input_textfield.text()):
            PopupWindow("warning",
                        "A bemeneti IP cím/maszk mező nem lehet üres!",
                        self.input_textfield)
        elif self.dec_to_bin_button.isChecked():
            if is_correct_any_ip_dec(self.input_textfield.text()):
                self.output_textfield.setText(dec_to_bin(self.input_textfield.text()))
            else:
                PopupWindow("warning",
                            "Érvénytelen decimális IP cím vagy maszk! Ellenőrizd!",
                            self.input_textfield)
        else:
            if is_correct_any_ip_bin(self.input_textfield.text()):
                self.output_textfield.setText(bin_to_dec(self.input_textfield.text()))
            else:
                PopupWindow("warning",
                            "Érvénytelen bináris IP cím vagy maszk! Ellenőrizd!",
                            self.input_textfield)


def dec_to_bin(ip_address):
    binary_format = ""
    for octet in ip_address.split("."):
        binary_format += f'{bin(int(octet)).replace("0b", "").rjust(8, "0")}.'
    return binary_format[:-1]


def copy_action(input_field_text):
    if input_field_text:
        copy(input_field_text)


def get_corrected_number(number):
    only_zeros = True
    for i in number:
        if not i == "0":
            only_zeros = False
    if not only_zeros:
        count_zero = 0
        if number[0] == "0":
            for i in number:
                if i == "0":
                    count_zero += 1
                if not i == "0":
                    break
            return number[count_zero:]
        return number
    return "0"


def bin_to_dec(ip_address_bin):
    decimal_format = ""
    for octet in ip_address_bin.split("."):
        decimal_format += f"{int(octet, 2)}."
    return decimal_format[:-1]
