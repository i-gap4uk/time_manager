from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import uic


class AboutWindow(QWidget):
    def __init__(self, resourcesManager):
        self._resourcesManager = resourcesManager
        QWidget.__init__(self)
        uic.loadUi("forms/aboutWindow.ui", self)
        self.image_label.setPixmap(QPixmap(self._resourcesManager.get_about_image()))

    def show(self):
        super().show()git stash
