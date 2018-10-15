from PyQt5.QtCore import QSettings


class SettingsManager:
    __settings = {}

    def __init__(self):
        self.__persistence = QSettings("settings.conf", QSettings.NativeFormat)
        self.read_persistence()

    def __set_settings(self):
        self.__set_main_window_settings()
        self.__set_file_manager_settings()
        self.__set_mail_manager()

    def __set_mail_manager(self):
        self.__persistence.setValue("LetterTheme/LETTER_THEME", self.__settings['letter_theme'])

    def __set_main_window_settings(self):
        self.__persistence.setValue("MainWindow/MIN_TO_TRAY", self.__settings['min_to_tray'])

    def __set_file_manager_settings(self):
        self.__persistence.setValue("OrderName/ORDER_NAME", self.__settings['order_name'])

    def __read_mail_manager_settings(self):
        self.__settings['letter_theme'] = self.__persistence.value(
            "LetterTheme/LETTER_THEME", "[You domain][OVERTIMES]: You name")

    def __read_main_window_settings(self):
        self.__settings['min_to_tray'] = self.__persistence.value(
            "MainWindow/MIN_TO_TRAY", False, type=bool)

    def __read_file_manager_settings(self):
        self.__settings['order_name'] = self.__persistence.value(
            "OrderName/ORDER_NAME", "overtimes")

    def read_persistence(self):
        self.__read_main_window_settings()
        self.__read_file_manager_settings()
        self.__read_mail_manager_settings()

    def write_persistence(self):
        self.__set_settings()
        self.__persistence.sync()

    def get_settings(self):
        return self.__settings
