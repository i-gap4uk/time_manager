#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from scripts.mainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("resources/images/app_icon_os.png"))
    app.setQuitOnLastWindowClosed(False)

    main_window = MainWindow()

    screen = app.primaryScreen()
    size = screen.size()
    x = (size.width() / 2) - (main_window.width() / 2)
    y = (size.height() / 2) - (main_window.height() / 2)

    main_window.move(x, y)
    main_window.show()

    sys.exit(app.exec_())

