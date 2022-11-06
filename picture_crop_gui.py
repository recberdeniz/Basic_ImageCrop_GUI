import sys
import os

from PyQt5 import QtWidgets, QtGui, QtCore

# This application is written by @recberdeniz to make a basic image crop process on basic GUI with PyQt5
# In this application there is a main window includes label as an image frame, open button, clip button, save button
# and clear button. With using a open button, user can load an image file to the frame(label) and getting a mouse
# position going to be active that means when user click 2 different points on the frame, application going to get
# this two pixel value each click and create a rectangle accordingly with this 2 different point values. When user click
# the clip button, accordingly to rectangle, image going to cropped. Cropping function has some controls that user
# firstly click on left bottom, right bottom, right top or left top of the rectangle with in the bounds of possibility
# rectangle parameters going to change. Save button using for saving the cropped image with file dialog and user
# have to insert a extend of file for example (cropped_image.png, cropped_image.jpg, cropped.tif). Lastly, clear
# button using for clear a label that use as image frame. Loaded image sizes might be different, that's why I did not
# set the image frame size

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Crop Application")
        self.init_ui()
        self.count = True # mouse position value control
        self.x = 0 # First mouse position x-value
        self.y = 0 # First mouse position y-value

    def init_ui(self):
# GUI widgets initilalize
        self.image_frame = QtWidgets.QLabel()
        self.image_frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.open_button = QtWidgets.QPushButton("Open")
        self.clip_button = QtWidgets.QPushButton("Clip")
        self.save_button = QtWidgets.QPushButton("Save")
        self.clear_button = QtWidgets.QPushButton("Clear")
# Horizontal box layout for GUI
        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addWidget(self.open_button)
        h_box.addWidget(self.clip_button)
        h_box.addWidget(self.save_button)
        h_box.addWidget(self.clear_button)
        h_box.addStretch()

# Vertical box layout for GUI
        v_box = QtWidgets.QVBoxLayout()

        v_box.addStretch()
        v_box.addWidget(self.image_frame)
        v_box.addStretch()
        v_box.addLayout(h_box)

        self.setLayout(v_box)

# Button Event functions
        self.open_button.clicked.connect(self.bttn_open)
        self.clear_button.clicked.connect(self.bttn_clear)
        self.clip_button.clicked.connect(self.bttn_clip)
        self.image_frame.mousePressEvent = self.getpos # Getting a mouse position function
        self.save_button.clicked.connect(self.bttn_save)

        self.show()

# Open button function
    def bttn_open(self):

        self.folder_name = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", os.getenv("HOME"))

# Image shrink to fit in frame
        pixmap = QtGui.QPixmap(self.folder_name[0])
        width = pixmap.width()
        height = pixmap.height()
        new_width = width / 2
        new_height = height / 2
        self.new_pixmap = pixmap.scaled(int(new_width), int(new_height), QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.image_frame.setPixmap(self.new_pixmap)
        self.resize(self.new_pixmap.width(), self.new_pixmap.height())

# Get mouse position function
    def getpos(self, event):
        self.x = event.pos().x()
        self.y = event.pos().y()
        if self.count == True:
            self.beginx = self.x
            self.beginy = self.y
            self.count = False

# Clear button function
    def bttn_clear(self):

        self.image_frame.clear()
        self.x = 0
        self.y = 0
        self.beginx = 0
        self.beginy = 0
        self.count = True

# Clip button fuction
    def bttn_clip(self):

        new_width = abs(self.x - self.beginx)
        new_height = abs(self.y - self.beginy)
        if self.x > self.beginx and self.y > self.beginy:
            rec = QtCore.QRect(self.beginx, self.beginy, new_width, new_height)

        elif self.beginx > self.x and self.beginy > self.y:
            rec = QtCore.QRect(self.x, self.y, new_width, new_height)

        elif self.beginx > self.x and self.y > self.beginy:
            rec = QtCore.QRect(self.x, self.beginy, new_width, new_height)

        else:
            rec = QtCore.QRect(self.beginx, self.y, new_width, new_height)

        self.pixmap = self.new_pixmap.copy(rec)
        self.image_frame.setPixmap(self.pixmap)

# Save button function
    def bttn_save(self):
        foldername_split = list()
        find_extend = list()
        exact_name = list()
        exact_extend = list()
        folder_name = QtWidgets.QFileDialog.getSaveFileName(self, "Save File", os.getenv("HOME"))

        foldername_split.append(folder_name[0].split("/"))

        for i in foldername_split:
            find_extend.append(i[-1])

        exact_name.append(find_extend[0].split("."))
        for i in exact_name:
            for j in i:
                exact_extend.append(j)

        self.pixmap.save(folder_name[0], exact_extend[-1])


app = QtWidgets.QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
