# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mod1_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from ctypes.wintypes import RGB
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPixmap, QImage, QColor, QPixelFormat
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QAction, QMainWindow, QSlider, QPushButton, QToolTip, QApplication
from PIL import Image, ImageOps, ImageEnhance, ImageColor
from PIL.ImageQt import ImageQt
import cv2
import numpy as np


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Mod1_design.ui', self)

        self.tabWidget.currentChanged.connect(self.tabChanged)

        self.openButton = self.findChild(QtWidgets.QPushButton, 'openButton')
        self.openButton.clicked.connect(self.loadImage)
        self.copyButton = self.findChild(QtWidgets.QPushButton, 'copyButton')
        self.copyButton.clicked.connect(self.copyImage)
        # self.exitButton = self.findChild(QtWidgets.QPushButton, 'exitButton')
        # self.exitButton.clicked.connect(MainWindow.close)

        #radio button
        self.btnRed = self.findChild(QtWidgets.QRadioButton, 'btnRed')
        self.btnRed.clicked.connect(self.convertRed)
        self.btnGreen = self.findChild(QtWidgets.QRadioButton, 'btnGreen')
        self.btnGreen.clicked.connect(self.convertGreen)
        self.btnBlue = self.findChild(QtWidgets.QRadioButton, 'btnBlue')
        self.btnBlue.clicked.connect(self.convertBlue)
        self.btnCyn = self.findChild(QtWidgets.QRadioButton, 'btnCyn')
        self.btnCyn.clicked.connect(self.convertCyan)
        self.btnMagenta = self.findChild(QtWidgets.QRadioButton, 'btnMagenta')
        self.btnMagenta.clicked.connect(self.convertMagenta)
        self.btnYellow = self.findChild(QtWidgets.QRadioButton, 'btnYellow')
        self.btnYellow.clicked.connect(self.convertYellow)

        # self.show()

    def tabChanged(self):
        print("tab change to:", self.tabWidget.currentIndex())
    def loadImage(self):
        self.namaImg, typeimg= QFileDialog.getOpenFileName(self.centralwidget, "Open Image", "", "*.jpg;;*.bmp;;All Files(*)")
        jpg = QPixmap(self.namaImg)

        self.pictureBox.setPixmap(jpg)

    def copyImage(self):
        img = Image.open(self.namaImg)
        width, height= img.size

        for row in range(height):
            for col in range(width):
                img.getpixel((col,row))

        img.save("copyim.jpg")     
        jpg=QPixmap("copyim.jpg")
        self.pictureBox2.setPixmap(jpg)
        # self.pictureBox3.setPixmap(jpg)

    def convertRed(self):
        img = cv2.imread(self.namaImg, cv2.IMREAD_UNCHANGED)
        print(img.shape)

        red_channel = img[:,:,2]
        red_img = np.zeros(img.shape)
        red_img[:,:,2] = red_channel

        cv2.imwrite("hasilConvert.jpg", red_img) 
        jpg=QPixmap("hasilConvert.jpg")
        self.pictureBox2.setPixmap(jpg)
        # img = Image.open(self.namaImg).convert("L")
        # red=  ImageOps.colorize(img, black ="red", white ="white")
        # gImage = ImageQt(red)
        # # width, height= img.size
        # # for row in range(height):
        # #     for col in range(width):
        # #          img.getpixel((col,row))
        # #         #  newColor = ImageColor.getrgb("red")
        # #          img.putpixel((col,row),(255,0,0))
                 
        # gImage.save("hasilConvert.jpg")     
        # jpg=QPixmap("hasilConvert.jpg")
        # self.pictureBox2.setPixmap(jpg)
        
    def convertGreen(self):
        img = cv2.imread(self.namaImg, cv2.IMREAD_UNCHANGED)
        print(img.shape)
        #BGR, 0=blue, 1=Greed, 2=Blue
        green_channel = img[:,:,1]
        green_img = np.zeros(img.shape)
        green_img[:,:,1] = green_channel

        cv2.imwrite("hasilConvert.jpg", green_img) 
        jpg=QPixmap("hasilConvert.jpg")
        self.pictureBox2.setPixmap(jpg)

    def convertBlue(self):
        img = cv2.imread(self.namaImg, cv2.IMREAD_UNCHANGED) 
        print(img.shape)
        blue_channel = img[:,:,0] 
        blue_img = np.zeros(img.shape)
        blue_img[:,:,0] = blue_channel 

        #save image
        cv2.imwrite("hasilConvert.jpg", blue_img) 
        jpg=QPixmap("hasilConvert.jpg")
        self.pictureBox2.setPixmap(jpg)
   
    def convertCyan(self):
        img = cv2.imread(self.namaImg, cv2.IMREAD_UNCHANGED)
        print(img.shape)
        
        img[:,:,2] = np.zeros([img.shape[0], img.shape[1]])

        #save image
        cv2.imwrite("hasilConvert.jpg", img) 
        jpg=QPixmap("hasilConvert.jpg")
        self.pictureBox3.setPixmap(jpg)
    
    def convertMagenta(self):
        img = cv2.imread(self.namaImg, cv2.IMREAD_UNCHANGED)
        print(img.shape)

        img[:,:,1] = np.zeros([img.shape[0], img.shape[1]])

        #save image
        cv2.imwrite("hasilConvert.jpg", img) 
        jpg=QPixmap("hasilConvert.jpg")
        self.pictureBox3.setPixmap(jpg)
    
    def convertYellow(self):
        img = cv2.imread(self.namaImg, cv2.IMREAD_UNCHANGED)
        print(img.shape)
        img[:,:,0] = np.zeros([img.shape[0], img.shape[1]])

        #save image
        cv2.imwrite("hasilConvert.jpg", img) 
        jpg=QPixmap("hasilConvert.jpg")
        self.pictureBox3.setPixmap(jpg)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    # ui.setupUi(MainWindow)
    ui.show()
    sys.exit(app.exec_())
