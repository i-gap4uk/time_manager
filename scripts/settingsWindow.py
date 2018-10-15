from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt


class SettingsWindow(QWidget):
    __changed = False

    def __init__(self, settings_manager):
        QWidget.__init__(self)
        uic.loadUi("forms/settingsWindow.ui", self)
        self.__settingsManager = settings_manager
        self.__init_form()
        self.__connect_signals()

    def __init_form(self):
        self.ok_btn.setEnabled(False)
        self.minToTray.setCheckState(Qt.Checked if self.__settingsManager.get_settings()['min_to_tray']
                                     else Qt.Unchecked)
        self.orderName.setText(self.__settingsManager.get_settings()['order_name'])
        self.letterTheme.setText(self.__settingsManager.get_settings()['letter_theme'])

    def __connect_signals(self):
        self.minToTray.pressed.connect(self.__settings_changed)
        self.orderName.textChanged.connect(self.__settings_changed)
        self.letterTheme.textChanged.connect(self.__settings_changed)
        self.ok_btn.pressed.connect(self.__save_changes)
        self.cancel_btn.pressed.connect(self.close)

    def __settings_changed(self):
        self.__changed = True
        self.ok_btn.setEnabled(True)
        self.__settingsManager.get_settings()['min_to_tray'] = self.minToTray.isChecked()
        self.__settingsManager.get_settings()['order_name'] = self.orderName.text()
        self.__settingsManager.get_settings()['letter_theme'] = self.letterTheme.text()

        self.__settingsManager.write_persistence()

    def closeEvent(self, QCloseEvent):
        if self.__changed is True:
            result = QMessageBox.question(self, "Exit", "Exit without saving?",
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if result == QMessageBox.Yes:
                QCloseEvent.accept()
            else:
                QCloseEvent.ignore()
        else:
            QCloseEvent.accept()

    def __save_changes(self):
        self.__settings_changed()
        self.__changed = False
        self.close()

    def show(self):
        self.__init_form()
        super().show()
