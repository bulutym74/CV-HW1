import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QPushButton, QGroupBox, QAction, QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        loadUi('hist_matching.ui', self)

        self.actionOpen_Input.triggered.connect(self.openInputImage)
        self.actionOpen_Target.triggered.connect(self.openTargetImage)
        self.actionExit.triggered.connect(self.exitApp)


    def openInputImage(self):
        pixmap = QPixmap('color1.png')
        self.img_input.setPixmap(pixmap)

    def openTargetImage(self):
        pixmap = QPixmap('color2.png')
        self.img_target.setPixmap(pixmap)

    def exitApp(self):
        sys.exit(0)


app = QApplication(sys.argv)
form = App()
form.show()
app.exec()

