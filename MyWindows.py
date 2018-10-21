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
from matplotlib import pyplot as plt
from PIL import Image
import histogram as h
import cumulative_histogram as ch

class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        loadUi('hist_matching.ui', self)

        self.actionOpen_Input.triggered.connect(self.openInputImage)
        self.actionOpen_Target.triggered.connect(self.openTargetImage)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionEqualize_Histogram.triggered.connect(self.plotHistogram)

    def openInputImage(self):
        pixmap = QPixmap("color1.png")
        self.img_input.setPixmap(pixmap)
        self.calcHistogramInput()

    def calcHistogramInput(self):

        def getRed(redVal):

            return '#%02x%02x%02x' % (redVal, 0, 0)

        def getGreen(greenVal):

            return '#%02x%02x%02x' % (0, greenVal, 0)

        def getBlue(blueVal):

            return '#%02x%02x%02x' % (0, 0, blueVal)

        image = Image.open("color1.png")
        image.putpixel((0, 1), (1, 1, 5))
        image.putpixel((0, 2), (2, 1, 5))

        histogram = image.histogram()

        l1 = histogram[0:256]
        l2 = histogram[256:512]
        l3 = histogram[512:768]

        for i in range(0, 256):
            plt.bar(i, l1[i], color=getRed(i), edgecolor=getRed(i), alpha=0.3)

        plt.savefig("input_r.png")
        pixmap = QPixmap("input_r.png")
        self.hist_input_r.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l2[i], color=getGreen(i), edgecolor=getGreen(i), alpha=0.3)

        plt.savefig("input_g.png")
        pixmap = QPixmap("input_g.png")
        self.hist_input_g.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l3[i], color=getBlue(i), edgecolor=getBlue(i), alpha=0.3)

        plt.savefig("input_b.png")
        pixmap = QPixmap("input_b.png")
        self.hist_input_b.setPixmap(pixmap)
        plt.close()


        # img = cv2.imread("color1.png")
        # plt.close()
        # color = ('b', 'g', 'r')
        # for channel, col in enumerate(color):
        #     histr = cv2.calcHist([img], [channel], None, [256], [0, 256])
        #     plt.plot(histr, color=col)
        #     plt.xlim([0, 256])
        # plt.savefig("input_r.png")
        # pixmap = QPixmap("input_r.png")
        # self.hist_input_r.setPixmap(pixmap)
        #
        # img = cv2.imread("color1.png")
        # plt.close()
        # color = ('b', 'g', 'r')
        # for channel, col in enumerate(color):
        #     histr = cv2.calcHist([img], [channel], None, [256], [0, 256])
        #     plt.plot(histr, color=col)
        #     plt.xlim([0, 256])
        # plt.savefig("input_g.png")
        # pixmap = QPixmap("input_g.png")
        # self.hist_input_g.setPixmap(pixmap)
        #
        # img = cv2.imread("color1.png")
        # plt.close()
        # color = ('b', 'g', 'r')
        # for channel, col in enumerate(color):
        #     histr = cv2.calcHist([img], [channel], None, [256], [0, 256])
        #     plt.plot(histr, color=col)
        #     plt.xlim([0, 256])
        # plt.savefig("input_b.png")
        # pixmap = QPixmap("input_b.png")
        # self.hist_input_b.setPixmap(pixmap)

        # img = cv2.imread("color1.png")
        # b, g, r = cv2.split(img)
        #
        # plt.close()
        # plt.hist(b.ravel(), 256, [0, 256])
        # plt.savefig("input_r.png")
        # pixmap = QPixmap("input_r.png")
        # self.hist_input_r.setPixmap(pixmap)
        #
        # plt.close()
        # plt.hist(g.ravel(), 256, [0, 256])
        # plt.savefig("input_g.png")
        # pixmap = QPixmap("input_g.png")
        # self.hist_input_g.setPixmap(pixmap)
        #
        # plt.close()
        # plt.hist(r.ravel(), 256, [0, 256])
        # plt.savefig("input_b.png")
        # pixmap = QPixmap("input_b.png")
        # self.hist_input_b.setPixmap(pixmap)

    def openTargetImage(self):
        pixmap = QPixmap("color2.png")
        self.img_target.setPixmap(pixmap)
        self.calcHistogramTarget()

    def calcHistogramTarget(self):

        def getRed(redVal):

            return '#%02x%02x%02x' % (redVal, 0, 0)

        def getGreen(greenVal):

            return '#%02x%02x%02x' % (0, greenVal, 0)

        def getBlue(blueVal):

            return '#%02x%02x%02x' % (0, 0, blueVal)

        image = Image.open("color2.png")
        image.putpixel((0, 1), (1, 1, 5))
        image.putpixel((0, 2), (2, 1, 5))

        histogram = image.histogram()

        l1 = histogram[0:256]
        l2 = histogram[256:512]
        l3 = histogram[512:768]

        for i in range(0, 256):
            plt.bar(i, l1[i], color=getRed(i), edgecolor=getRed(i), alpha=0.3)

        plt.savefig("target_r.png")
        pixmap = QPixmap("target_r.png")
        self.hist_target_r.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l2[i], color=getGreen(i), edgecolor=getGreen(i), alpha=0.3)

        plt.savefig("target_g.png")
        pixmap = QPixmap("target_g.png")
        self.hist_target_g.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l3[i], color=getBlue(i), edgecolor=getBlue(i), alpha=0.3)

        plt.savefig("target_b.png")
        pixmap = QPixmap("target_b.png")
        self.hist_target_b.setPixmap(pixmap)
        plt.close()

        # plt.close()
        # img = cv2.imread("color2.png")
        # color = ('b', 'g', 'r')
        # for channel, col in enumerate(color):
        #     histr = cv2.calcHist([img], [channel], None, [256], [0, 256])
        #     plt.plot(histr, color=col)
        #     plt.xlim([0, 256])
        #
        # plt.title("Histogram of TARGET image")
        #
        # plt.savefig("test.png")
        # plt.show()

    def exitApp(self):
        sys.exit(0)

    def plotHistogram(self):
        img = cv2.imread('color1.png', cv2.IMREAD_GRAYSCALE)
        img_ref = cv2.imread('color2.png', cv2.IMREAD_GRAYSCALE)

        height = img.shape[0]
        width = img.shape[1]
        pixels = width * height

        height_ref = img_ref.shape[0]
        width_ref = img_ref.shape[1]
        pixels_ref = width_ref * height_ref

        hist = h.histogram(img)
        hist_ref = h.histogram(img_ref)

        cum_hist = ch.cumulative_histogram(hist)
        cum_hist_ref = ch.cumulative_histogram(hist_ref)

        prob_cum_hist = cum_hist / pixels

        prob_cum_hist_ref = cum_hist_ref / pixels_ref

        K = 256
        new_values = np.zeros((K))

        for a in np.arange(K):
            j = K - 1
            while True:
                new_values[a] = j
                j = j - 1
                if j < 0 or prob_cum_hist[a] > prob_cum_hist_ref[j]:
                    break

        for i in np.arange(height):
            for j in np.arange(width):
                a = img.item(i, j)
                b = new_values[a]
                img.itemset((i, j), b)

        # img.savefig("result.png")
        cv2.imwrite("result.png", img)
        pixmap = QPixmap("result.png")
        self.img_result.setPixmap(pixmap)

        # cv2.imwrite('images/hist_matched.jpg', img)
        #
        # cv2.imshow('image', img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        self.calcHistogramResult()


    def calcHistogramResult(self):

        def getRed(redVal):

            return '#%02x%02x%02x' % (redVal, 0, 0)

        def getGreen(greenVal):

            return '#%02x%02x%02x' % (0, greenVal, 0)

        def getBlue(blueVal):

            return '#%02x%02x%02x' % (0, 0, blueVal)

        image = Image.open("result.png")
        image.putpixel((0, 1), (1, 1, 5))
        image.putpixel((0, 2), (2, 1, 5))

        histogram = image.histogram()

        l1 = histogram[0:256]
        l2 = histogram[256:512]
        l3 = histogram[512:768]

        for i in range(0, 256):
            plt.bar(i, l1[i], color=getRed(i), edgecolor=getRed(i), alpha=0.3)

        plt.savefig("result_r.png")
        pixmap = QPixmap("result_r.png")
        self.hist_result_r.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l2[i], color=getGreen(i), edgecolor=getGreen(i), alpha=0.3)

        plt.savefig("result_g.png")
        pixmap = QPixmap("result_g.png")
        self.hist_result_g.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l3[i], color=getBlue(i), edgecolor=getBlue(i), alpha=0.3)

        plt.savefig("result_b.png")
        pixmap = QPixmap("result_b.png")
        self.hist_result_b.setPixmap(pixmap)
        plt.close()




app = QApplication(sys.argv)
form = App()
form.show()
app.exec()

