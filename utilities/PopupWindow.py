from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMessageBox


class PopupWindow(QMessageBox):
    def __init__(self, popup_type, text, focus):
        super(PopupWindow, self).__init__()

        msgbox = self
        msgbox.setWindowIcon(QIcon("static/images/main_icon.png"))
        title = "Network Assistant"

        if popup_type == "warning":
            msgbox.warning(self, title, text)
            focus.setFocus()
