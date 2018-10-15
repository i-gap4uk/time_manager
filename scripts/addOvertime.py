from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDateTime, pyqtSignal, Qt

from PyQt5.QtGui import QPixmap

from PyQt5 import uic


class AddOvertimeWindow(QWidget):

    def __init__(self, db_manager, resourcesManager):
        QWidget.__init__(self)
        uic.loadUi("forms/addOvertimeWindow.ui", self)

        self.__resourcesManager = resourcesManager

        # define private members(fields values)
        self.__db_manager = db_manager
        self.__date = ""
        self.__hours_count = 0
        self.__overtime_note = ""

        self.__init_form()
        self.__connect_all_signals()

    data_collected = pyqtSignal(str, int, str, name='dataCollected')

    def __init_form(self):
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.overtime_level.setPixmap(QPixmap(self.__resourcesManager.get_overtimes_level_image(1)))

    def __close_form(self):
        self.dateEdit.setDateTime(QDateTime.currentDateTime())
        self.hours_counter.setValue(0)
        self.noteText.setPlainText("")
        self.close()

    def __connect_all_signals(self):
        self.hours_counter.valueChanged.connect(self.__change_overtime_level)
        self.ok_btn.pressed.connect(self.__apply_overtime)
        self.cancel_btn.pressed.connect(self.__close_form)

    def __change_overtime_level(self, level):
        if level >= 0 and level <= 6:
            self.overtime_level.setPixmap(QPixmap(self.__resourcesManager.get_overtimes_level_image(1)))

        elif level > 6 and level <= 12:
            self.overtime_level.setPixmap(QPixmap(self.__resourcesManager.get_overtimes_level_image(2)))

        elif (level > 12 and level <= 18):
            self.overtime_level.setPixmap(QPixmap(self.__resourcesManager.get_overtimes_level_image(3)))

        elif (level > 18 and level <= 24):
            self.overtime_level.setPixmap(QPixmap(self.__resourcesManager.get_overtimes_level_image(4)))

    def __collect_data(self):
        self.__date = self.dateEdit.date().toString(Qt.ISODate)
        self.__hours_count = self.hours_counter.value()
        self.__overtime_note = self.noteText.toPlainText()

    def __apply_overtime(self):
        self.__collect_data()
        str = self.__db_manager.insert_data(self.__date, self.__hours_count, self.__overtime_note)

        if str[0] == 'error':
            QMessageBox.critical(self, "Error", "You cannot add to this date")
        elif str[0] == 'done':
            QMessageBox.information(self,"Well done", "Overetime was added")
            self.__close_form()

    def show(self):
        super().show()





