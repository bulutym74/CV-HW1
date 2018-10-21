import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import numpy as np
import cv2
from PyQt5.uic import loadUi
from matplotlib import pyplot as plt
from PIL import Image

class App(QMainWindow):

    def __init__(self):
        super(App, self).__init__()
        loadUi('hist_matching.ui', self)

        self.actionOpen_Input.triggered.connect(self.openInputImage)
        self.actionOpen_Target.triggered.connect(self.openTargetImage)
        self.actionExit.triggered.connect(self.exitApp)
        self.actionEqualize_Histogram.triggered.connect(self.matchHistogram)

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
        image.putpixel((0, 1), (1, 1, 5))               #Modify the color of two pixels
        image.putpixel((0, 2), (2, 1, 5))

        histogram = image.histogram()                   #Get the color histogram of the image

        l1 = histogram[0:256]           #Red counts
        l2 = histogram[256:512]         #Blue counts
        l3 = histogram[512:768]         #Green counts


        for i in range(0, 256):
            plt.bar(i, l1[i], color=getRed(i), edgecolor=getRed(i), alpha=0.3)              # R histogram

        plt.savefig("input_r.png")
        pixmap = QPixmap("input_r.png")
        self.hist_input_r.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l2[i], color=getGreen(i), edgecolor=getGreen(i), alpha=0.3)          # G histogram

        plt.savefig("input_g.png")
        pixmap = QPixmap("input_g.png")
        self.hist_input_g.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l3[i], color=getBlue(i), edgecolor=getBlue(i), alpha=0.3)            # B histogram

        plt.savefig("input_b.png")
        pixmap = QPixmap("input_b.png")
        self.hist_input_b.setPixmap(pixmap)
        plt.close()


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
        image.putpixel((0, 1), (1, 1, 5))       #Modify the color of two pixels
        image.putpixel((0, 2), (2, 1, 5))

        histogram = image.histogram()       #Get the color histogram of the image

        l1 = histogram[0:256]           #Red counts
        l2 = histogram[256:512]         #Blue counts
        l3 = histogram[512:768]         #Green counts

        for i in range(0, 256):
            plt.bar(i, l1[i], color=getRed(i), edgecolor=getRed(i), alpha=0.3)     # R histogram

        plt.savefig("target_r.png")
        pixmap = QPixmap("target_r.png")
        self.hist_target_r.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l2[i], color=getGreen(i), edgecolor=getGreen(i), alpha=0.3)  # G histogram

        plt.savefig("target_g.png")
        pixmap = QPixmap("target_g.png")
        self.hist_target_g.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l3[i], color=getBlue(i), edgecolor=getBlue(i), alpha=0.3)    # B histogram

        plt.savefig("target_b.png")
        pixmap = QPixmap("target_b.png")
        self.hist_target_b.setPixmap(pixmap)
        plt.close()


    def exitApp(self):
        sys.exit(0)

    def matchHistogram(self):

        def zeros(dict):
            for i in range(256):
                dict[i] = 0
            return dict

        def frequency(channel, dict):
            dictionary = zeros(dict)
            rows = channel.shape[0]
            cols = channel.shape[1]
            for i in range(rows):
                for j in range(cols):
                    dictionary[channel[i, j]] += 1

            return dictionary

        def color(name):

            color = cv2.imread(name)

            blue, green, red = cv2.split(color)
            size = color.size / 3

            blue_dict = {}
            green_dict = {}
            red_dict = {}

            blue_dict = frequency(blue, blue_dict)
            green_dict = frequency(green, green_dict)
            red_dict = frequency(red, red_dict)

            blue_array = np.asarray(list(blue_dict.values()))
            green_array = np.asarray(list(green_dict.values()))
            red_array = np.asarray(list(red_dict.values()))

            blue_array = np.cumsum(blue_array)
            green_array = np.cumsum(green_array)
            red_array = np.cumsum(red_array)

            blue_array = blue_array / size
            green_array = green_array / size
            red_array = red_array / size

            liste = []
            liste.append(blue_array)
            liste.append(green_array)
            liste.append(red_array)
            return liste

        def matching(img1, img2):
            table = [0] * 256
            j = 0
            for i in range(255):
                while j < 255 and img2[j + 1] < img1[i + 1]:
                    j += 1
                table[i + 1] = j

            return table

        def LUT(color1, table_b, table_g, table_r):
            blue, green, red = cv2.split(color1)
            rows, cols, channel = color1.shape

            for i in range(rows):
                for j in range(cols):
                    blue[i, j] = table_b[blue[i, j]]
                    green[i, j] = table_g[green[i, j]]
                    red[i, j] = table_r[red[i, j]]

            return cv2.merge((blue, green, red))

        name1 = "color1.png"
        name2 = "color2.png"
        image = cv2.imread(name1)

        l1 = color(name1)
        l2 = color(name2)

        table_b = matching(l1[0], l2[0])
        table_g = matching(l1[1], l2[1])
        table_r = matching(l1[2], l2[2])

        img = LUT(image, table_b, table_g, table_r)
        cv2.imwrite("result.png", img)
        pixmap = QPixmap("result.png")
        self.img_result.setPixmap(pixmap)
        self.calcHistogramResult()


    def calcHistogramResult(self):

        def getRed(redVal):

            return '#%02x%02x%02x' % (redVal, 0, 0)

        def getGreen(greenVal):

            return '#%02x%02x%02x' % (0, greenVal, 0)

        def getBlue(blueVal):

            return '#%02x%02x%02x' % (0, 0, blueVal)

        image = Image.open("result.png")
        image.putpixel((0, 1), (1, 1, 5))               #Modify the color of two pixels
        image.putpixel((0, 2), (2, 1, 5))

        histogram = image.histogram()                   #Get the color histogram of the image

        l1 = histogram[0:256]  # Red counts
        l2 = histogram[256:512]  # Blue counts
        l3 = histogram[512:768]  # Green counts

        for i in range(0, 256):
            plt.bar(i, l1[i], color=getRed(i), edgecolor=getRed(i), alpha=0.3)          # R histogram

        plt.savefig("result_r.png")
        pixmap = QPixmap("result_r.png")
        self.hist_result_r.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l2[i], color=getGreen(i), edgecolor=getGreen(i), alpha=0.3)      # G histogram

        plt.savefig("result_g.png")
        pixmap = QPixmap("result_g.png")
        self.hist_result_g.setPixmap(pixmap)
        plt.close()

        for i in range(0, 256):
            plt.bar(i, l3[i], color=getBlue(i), edgecolor=getBlue(i), alpha=0.3)        # B histogram

        plt.savefig("result_b.png")
        pixmap = QPixmap("result_b.png")
        self.hist_result_b.setPixmap(pixmap)
        plt.close()




app = QApplication(sys.argv)
form = App()
form.show()
app.exec()

