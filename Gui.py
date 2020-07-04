# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Youtube downloader.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Downloader
from threading import Thread
import os

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.setEnabled(True)
        Form.resize(1054, 192)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setStyleSheet("background-color: rgb(54, 56, 61);")
        Form.setWindowFilePath("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setStyleSheet("color: rgb(97, 242, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.play_lista_link = QtWidgets.QLineEdit(Form)
        self.play_lista_link.setStyleSheet("color: rgb(97, 242, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.play_lista_link.setText("")
        self.play_lista_link.setObjectName("play_lista_link")
        self.horizontalLayout.addWidget(self.play_lista_link)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dir_label = QtWidgets.QLabel(Form)
        self.dir_label.setStyleSheet("color: rgb(97, 242, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.dir_label.setObjectName("dir_label")
        self.horizontalLayout_2.addWidget(self.dir_label)
        self.folder_where_to_save = QtWidgets.QLineEdit(Form)
        self.folder_where_to_save.setStyleSheet("color: rgb(97, 242, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.folder_where_to_save.setObjectName("folder_where_to_save")
        self.horizontalLayout_2.addWidget(self.folder_where_to_save)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setStyleSheet("color: rgb(97, 242, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setStyleSheet("color: rgb(97, 242, 255);\n"
"font: 18pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SONG URL / PLAYLIST URL"))
        self.dir_label.setText(_translate("Form", "FOLDER WHERE TO SAVE SONGS"))
        self.pushButton.setText(_translate("Form", "Download"))
        self.pushButton.clicked.connect(self.start)


    def start(self):
        self.get_link = str(self.play_lista_link.text())
        full_link = [self.get_link , ]
        folder = "ZA SAMPLOVANJE"
        self.max_Counter = Downloader.index_finder(full_link)
        ar = (full_link , folder)
        self.starter = Thread(target=self.download , args=ar)
        self.starter.start()
        # progress = Thread(target=self.progressBarUpdater)
        # progress.start()



    def progressBarUpdater(self):
        try:
            while self.starter.is_alive():
                import time
                time.sleep(1)
                try:
                    with open('counter.txt', 'r') as file:
                        test = file.readline()
                        self.progressBar.setValue(int(int(test) / self.max_Counter * 100))
                except:
                    pass
        except Exception as a:
            print(a)



    def download(self, full_lista, direct):
        Downloader.downloader(full_lista , direct)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
