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
    x = int((size.width() / 2) - (main_window.width() / 2))
    y = int((size.height() / 2) - (main_window.height() / 2))

    main_window.move(x, y)
    main_window.show()
    main_window.raise_()

    sys.exit(app.exec())

