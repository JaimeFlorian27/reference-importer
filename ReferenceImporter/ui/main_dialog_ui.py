# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui(object):
    def __init__(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(329, 409)
        self.verticalLayout_main = QVBoxLayout(Dialog)
        self.verticalLayout_main.setObjectName(u"verticalLayout_main")
        self.groupBox_input = QGroupBox(Dialog)
        self.groupBox_input.setObjectName(u"groupBox_input")
        self.gridLayout_input = QGridLayout(self.groupBox_input)
        self.gridLayout_input.setObjectName(u"gridLayout_input")
        self.label_video_file = QLabel(self.groupBox_input)
        self.label_video_file.setObjectName(u"label_video_file")

        self.gridLayout_input.addWidget(self.label_video_file, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_input)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_input.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.pushButton_fileExplorer_input = QPushButton(self.groupBox_input)
        self.pushButton_fileExplorer_input.setObjectName(u"pushButton_fileExplorer_input")

        self.gridLayout_input.addWidget(self.pushButton_fileExplorer_input, 1, 1, 1, 1)


        self.verticalLayout_main.addWidget(self.groupBox_input)

        self.groupBox_trim = QGroupBox(Dialog)
        self.groupBox_trim.setObjectName(u"groupBox_trim")
        self.groupBox_trim.setEnabled(True)
        self.gridLayout_trim = QGridLayout(self.groupBox_trim)
        self.gridLayout_trim.setObjectName(u"gridLayout_trim")
        self.label_start_trim = QLabel(self.groupBox_trim)
        self.label_start_trim.setObjectName(u"label_start_trim")

        self.gridLayout_trim.addWidget(self.label_start_trim, 0, 1, 1, 1)

        self.lineEdit_start_trim = QLineEdit(self.groupBox_trim)
        self.lineEdit_start_trim.setObjectName(u"lineEdit_start_trim")
        self.lineEdit_start_trim.setText('00:00:00')

        self.gridLayout_trim.addWidget(self.lineEdit_start_trim, 1, 1, 1, 1)

        self.lineEdit_end_trim = QLineEdit(self.groupBox_trim)
        self.lineEdit_end_trim.setObjectName(u"lineEdit_end_trim")
        self.lineEdit_end_trim.setText('00:00:00')

        self.gridLayout_trim.addWidget(self.lineEdit_end_trim, 1, 3, 1, 1)

        self.label_end_trim = QLabel(self.groupBox_trim)
        self.label_end_trim.setObjectName(u"label_end_trim")

        self.gridLayout_trim.addWidget(self.label_end_trim, 0, 3, 1, 1)


        self.verticalLayout_main.addWidget(self.groupBox_trim)

        self.groupBox_output = QGroupBox(Dialog)
        self.groupBox_output.setObjectName(u"groupBox_output")
        self.gridLayout_output = QGridLayout(self.groupBox_output)
        self.gridLayout_output.setObjectName(u"gridLayout_output")
        self.lineEdit_output_directory = QLineEdit(self.groupBox_output)
        self.lineEdit_output_directory.setObjectName(u"lineEdit_output_directory")

        self.gridLayout_output.addWidget(self.lineEdit_output_directory, 3, 0, 1, 3)

        self.spinBox_frameRate = QSpinBox(self.groupBox_output)
        self.spinBox_frameRate.setObjectName(u"spinBox_frameRate")
        self.spinBox_frameRate.setMinimum(1)
        self.spinBox_frameRate.setValue(24)

        self.gridLayout_output.addWidget(self.spinBox_frameRate, 4, 1, 1, 1)

        self.label_frameRate = QLabel(self.groupBox_output)
        self.label_frameRate.setObjectName(u"label_frameRate")

        self.gridLayout_output.addWidget(self.label_frameRate, 4, 0, 1, 1)

        self.checkBox_imagePlane = QCheckBox(self.groupBox_output)
        self.checkBox_imagePlane.setObjectName(u"checkBox_imagePlane")

        self.gridLayout_output.addWidget(self.checkBox_imagePlane, 4, 2, 1, 2)

        self.label_output_directory = QLabel(self.groupBox_output)
        self.label_output_directory.setObjectName(u"label_output_directory")

        self.gridLayout_output.addWidget(self.label_output_directory, 2, 0, 1, 1)

        self.pushButton_fileExplorer_output = QPushButton(self.groupBox_output)
        self.pushButton_fileExplorer_output.setObjectName(u"pushButton_fileExplorer_output")

        self.gridLayout_output.addWidget(self.pushButton_fileExplorer_output, 3, 3, 1, 1)

        self.label = QLabel(self.groupBox_output)
        self.label.setObjectName(u"label")

        self.gridLayout_output.addWidget(self.label, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox_output)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_output.addWidget(self.comboBox, 1, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox_output)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_output.addWidget(self.label_2, 0, 2, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox_output)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_output.addWidget(self.lineEdit_2, 1, 0, 1, 2)


        self.verticalLayout_main.addWidget(self.groupBox_output)

        self.pushButton_create_image_sequence = QPushButton(Dialog)
        self.pushButton_create_image_sequence.setObjectName(u"pushButton_create_image_sequence")

        self.verticalLayout_main.addWidget(self.pushButton_create_image_sequence)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox_input.setTitle(QCoreApplication.translate("Dialog", u"Input", None))
        self.label_video_file.setText(QCoreApplication.translate("Dialog", u"Video File", None))
        self.pushButton_fileExplorer_input.setText(QCoreApplication.translate("Dialog", u"Open...", None))
        self.groupBox_trim.setTitle(QCoreApplication.translate("Dialog", u"Trimming", None))
        self.label_start_trim.setText(QCoreApplication.translate("Dialog", u"Start", None))
        self.label_end_trim.setText(QCoreApplication.translate("Dialog", u"End", None))
        self.groupBox_output.setTitle(QCoreApplication.translate("Dialog", u"Output", None))
        self.label_frameRate.setText(QCoreApplication.translate("Dialog", u"Target Frame Rate", None))
        self.checkBox_imagePlane.setText(QCoreApplication.translate("Dialog", u"Create Image Plane", None))
        self.label_output_directory.setText(QCoreApplication.translate("Dialog", u"Output Directory", None))
        self.pushButton_fileExplorer_output.setText(QCoreApplication.translate("Dialog", u"Open...", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Sequence File Name", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u".jpg", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u".png", None))

        self.label_2.setText(QCoreApplication.translate("Dialog", u"File Extension", None))
        self.pushButton_create_image_sequence.setText(QCoreApplication.translate("Dialog", u"Create Image Sequence", None))
    # retranslateUi


if __name__ == "__main__":
    pass


