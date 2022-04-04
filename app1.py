from PyQt5.QtWidgets import QMainWindow,QPushButton,QLabel,QFileDialog,QApplication
from PyQt5 import uic,QtGui
from PyQt5.QtGui import QPixmap
import sys

from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from skimage.filters import frangi, hessian
import cv2
import numpy as np
from matplotlib import pyplot as plt


class UI(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        uic.loadUi("pyqt.ui",self)
        self.disply_width = 640
        self.display_height = 480
        self.button=self.findChild(QPushButton,"pushButton")
        self.label=self.findChild(QLabel,"label")
    
        self.button2=self.findChild(QPushButton,"pushButton_2")
        self.button3=self.findChild(QPushButton,"pushButton_3")

        self.label2=self.findChild(QLabel,"label_2")

        self.button.clicked.connect(self.clicker)
        self.button2.clicked.connect(self.clicker2)
        self.button3.clicked.connect(self.clicker3)


        self.show()
    def clicker(self):
        fname=QFileDialog.getOpenFileName(self,"Open File","c:\\","All Files (*);;")
        self.img=fname[0];
        
        self.pixmap=QPixmap(fname[0])
        self.label.setPixmap(self.pixmap)
    
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        # rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        rgb_image = cv_img
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def clicker2(self):
        img0=cv2.imread(self.img,)
        dim = (450, 450)
  
        # img0 = cv2.resize(img0, dim, interpolation = cv2.INTER_AREA)
        img0=self.filter1(img0)
        self.pixmap2=self.convert_cv_qt(img0)
        self.label2.setPixmap(self.pixmap2)
    def clicker3(self):
        img0=cv2.imread(self.img,)
        dim = (450, 450)
  
        # img0 = cv2.resize(img0, dim, interpolation = cv2.INTER_AREA)
        img0=self.filter2(img0)
        self.pixmap2=self.convert_cv_qt(img0)
        self.label2.setPixmap(self.pixmap2)
    def filter1(self,img):     
        return hessian(img)
    def filter2(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # remove noise
        img = cv2.GaussianBlur(gray,(3,3),0)
        sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  

        return cv2.cvtColor(sobely, cv2.COLOR_GRAY2BGR)

app=QApplication(sys.argv)
UIWindow=UI()
app.exec()