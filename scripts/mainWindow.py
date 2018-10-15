from PyQt5.QtWidgets import QMainWindow, QMenu, QAction, QSystemTrayIcon, qApp
from PyQt5.QtGui import QIcon

from PyQt5 import uic

from scripts.addOvertime import AddOvertimeWindow
from scripts.viewOvertime import ViewOvertimeWindow
from scripts.aboutWindow import AboutWindow
from scripts.settingsWindow import SettingsWindow
from scripts.dbManager import DbManager
from scripts.settingsManager import SettingsManager
from scripts.resourcesManager import ResourcesManager
from scripts.fileManager import FileManager


class MainWindow(QMainWindow):
    __tray_menu = None
    __tray_icon = None

    def __init__(self):
        super().__init__()
        uic.loadUi("forms/main_window.ui", self)
        self.__init_form()
        self.__init_managers()
        self.__init_actions()
        self.__init_tray_menu()

    def __init_form(self):
        self.menuBar().setNativeMenuBar(False)
        self.__init_tray_menu()

    def __init_tray_menu(self):
        self.__tray_icon = QSystemTrayIcon(QIcon("../resources/tray_icon.png"), self)
        self.__tray_icon.setIcon(QIcon("../resources/images/tray_icon.png"))
        self.__tray_menu = QMenu(self)

        show_action = QAction("Show", self)
        show_action.triggered.connect(self.show)
        add_action = QAction("Add Overtime", self)
        add_action.triggered.connect(self.__show_addovertime_window)
        view_action = QAction("View overtimes", self)
        view_action.triggered.connect(self.__show_viewovertime_window)
        settings_action = QAction("Settings", self)
        settings_action.triggered.connect(self.__show_settings_window)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(qApp.quit)

        self.__tray_menu.addAction(show_action)
        self.__tray_menu.addAction(add_action)
        self.__tray_menu.addAction(view_action)
        self.__tray_menu.addAction(settings_action)
        self.__tray_menu.addAction(exit_action)

        self.__tray_icon.setContextMenu(self.__tray_menu)
        self.__tray_icon.setToolTip("Click me!")

    def __init_managers(self):
        self.__settingsManager = SettingsManager()
        self.__fileManager = FileManager(self.__settingsManager)
        self.__resourcesManager = ResourcesManager()
        self.__dbManager = DbManager()

    def __init_actions(self):
        self.actionAdd_overtime.triggered.connect(self.__show_addovertime_window)
        self.actionView_overtime.triggered.connect(self.__show_viewovertime_window)
        self.actionSettings.triggered.connect(self.__show_settings_window)
        self.actionAbout.triggered.connect(self.__show_about_window)
        self.actionExit.triggered.connect(qApp.quit)

    def __show_addovertime_window(self):
        self.__addOverWin = AddOvertimeWindow(self.__dbManager, self.__resourcesManager)
        self.__addOverWin.show()

    def __show_viewovertime_window(self):
        self.__viewOverWin = ViewOvertimeWindow(self.__dbManager, self.__fileManager)
        self.__viewOverWin.show()

    def __show_about_window(self):
        self.__aboutWindow = AboutWindow(self.__resourcesManager)
        self.__aboutWindow.show()

    def __show_settings_window(self):
        self.__settings_window = SettingsWindow(self.__settingsManager)
        self.__settings_window.show()

    def closeEvent(self, closeEvent):
        if self.__settingsManager.get_settings()['min_to_tray'] is True:
            closeEvent.ignore()
            self.hide()
            self.__tray_icon.show()
        else:
            qApp.quit()

    def show(self):
        super().show()


