from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QGuiApplication
from PySide2.QtWidgets import QMessageBox, QStyle


class PopupWindow(QMessageBox):
    def __init__(self, popup_type, text, focus):
        super(PopupWindow, self).__init__()

        msgbox = self

        # Set window center of screen
        msgbox.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                self.size(),
                QGuiApplication.primaryScreen().availableGeometry(),
            ),
        )

        msgbox.setWindowIcon(QIcon("static/images/main_icon.png"))
        title = "Network Assistant"

        if popup_type == "warning":
            msgbox.warning(self, title, text)
            focus.setFocus()
