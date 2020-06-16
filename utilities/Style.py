def style():
    my_style = '''

QWidget {
    font-size: 12px;
}

QMainWindow {
    background-color: #2a2f38;
}

QGroupBox  {
    background-color: #2a2f38;
    color: white;
}

QTabWidget::pane {
    border: 1px solid white;
    background-color: #2a2f38;
}

QTabBar::tab {
    background-color: #636d7d;
    color: white;
}

QTabBar::tab:hover {
    background-color: #c1c7ce;
    color: black;
}

QTabBar::tab:selected {
    background-color: white;
    color: black;
}

QRadioButton {
    color: white;
}

QPushButton {
    background-color: #2a2f38;
    border: 1px solid white;
    border-radius: 2px;
    border-style: outset;
    color: white;
    min-width: 5em;
    padding: 6px;
}

QPushButton:hover {
    background-color: #636d7d;
    color: white;
}

QLabel {
    color: white;
    font-size: 13px;
}

QLineEdit {
    font-size: 15px;
}

QLineEdit:read-only {
    background-color: lightgreen;
}

QTableWidget {
    background-color: #272822;
    color: white;
    gridline-color: lightgray;
}

QTableWidget::item:hover {
    background-color: #007a99;
    color: white;
}

QHeaderView::section {
    background-color: #646464;
    color: white;
    border: 1px solid #fffff8;
    font-size: 9pt;
}

QProgressBar {
    text-align: center;
}

QProgressBar::chunk {
    background-color: DodgerBlue;
}

QRadioButton {    
    font-size: 11px;
    padding: 2px;
}

QRadioButton::indicator:unchecked {
   width: 7px;
    height: 7px;
    left: 1px;
    margin-right: 1px;
    background-color: white;
    border: 2px solid white;
    border-radius: 5px;
}

QRadioButton::indicator:unchecked:hover {
    width: 10px;
    height: 10px;
    left: -0.5px;
    bottom: -1.5px;
    border: 1px solid rgb(0, 120, 215);
    border-radius: 5px;    
}

QRadioButton::indicator:checked {
    width: 7px;
    height: 7px;
    left: 1px;
    margin-right: 1px;
    background-color: rgb(51, 51, 51);
    border: 2px solid white;
    border-radius: 5px;
}

QRadioButton::indicator:checked:hover {
    background-color: rgb(0, 120, 215);
}

    '''
    return my_style
