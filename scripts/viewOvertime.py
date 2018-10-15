from PyQt5 import uic

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import QDateTime, Qt


class ViewOvertimeWindow(QWidget):
    def __init__(self, dbManager, fileManager):
        QWidget.__init__(self)
        uic.loadUi("forms/viewOvertime.ui", self)
        self.__init_form()
        self.__table_items = []
        self.end_range.setDisabled(True)
        self.overtimes_table.setSortingEnabled(False)
        self.__db_manager = dbManager
        self.__file_manager = fileManager

    def __init_form(self):
        self.start_range.setDateTime(QDateTime.currentDateTime())
        self.end_range.setDateTime(QDateTime.currentDateTime().addDays(1))
        self.overtimes_table.setSortingEnabled(True)
        self.overtimes_table.sortByColumn(0, Qt.AscendingOrder)
        self.__connect_signals()

    def __connect_signals(self):
        self.show_btn.pressed.connect(self.__show_results)
        self.ok_btn.pressed.connect(self.__close_form)
        self.clear_btn.pressed.connect(self.__clear_form)
        self.create_order.pressed.connect(self.__save_order)

    def __show_results(self):
        if self.definite_date.isChecked() is True:
            date = self.start_range.date().toString(Qt.ISODate)
            overtimes = self.__db_manager.get_data_from_date(date)
            self.__set_data_to_listview(overtimes)

        elif self.date_range.isChecked() is True:
            startDate = self.start_range.date().toString(Qt.ISODate)
            endDate = self.end_range.date().toString(Qt.ISODate)
            overtimes = self.__db_manager.get_data_from_date_range(startDate, endDate)
            self.__set_data_to_listview(overtimes)

        else:
            data_list = self.__db_manager.get_from_all_time()
            self.__set_data_to_listview(data_list)

    def __set_data_to_listview(self, data_list):
        self.__clear_form()
        date = 0
        hours = 1
        note = 2
        total_hours = 0
        self.__table_items = data_list

        row = 0
        column = 0
        self.overtimes_table.setRowCount(len(data_list))
        for item in data_list:
            self.overtimes_table.setItem(row, column, QTableWidgetItem(item[date]))
            column += 1
            self.overtimes_table.setItem(row, column, QTableWidgetItem(str(item[hours])))
            total_hours += item[hours]
            column += 1
            self.overtimes_table.setItem(row, column, QTableWidgetItem(item[note]))
            column = 0
            row += 1
        self.total_hours.display(total_hours)
        self.overtimes_table.sortItems(date, Qt.AscendingOrder)

        if not self.__table_items:
            self.create_order.setEnabled(False)
        else:
            self.create_order.setEnabled(True)

    def __save_order(self):
        # TODO:maybe, give possibility for users to choose path to saving file?
        self.__file_manager.save_order(self.__table_items)
        QMessageBox.information(self, "Well done", "Order was created as:\n"
                                + self.__file_manager.get_order_path())

    def show(self):
        super().show()

    def __clear_form(self):
        self.overtimes_table.setRowCount(0)
        self.total_hours.display(0)
        self.create_order.setEnabled(False)
        self.__table_items.clear()

    def __close_form(self):
        self.close()






