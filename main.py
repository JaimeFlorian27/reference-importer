# -*- coding: utf-8 -*-
# Reference Importer v1.1, made by Jaime Florian
# Video Demonstration: https://www.youtube.com/watch?v=ObX9NU2BmZo

import os
import sys


from Qt import QtCore, QtGui
from Qt.QtWidgets import QDialog, QFileDialog, QApplication
from Qt import QtCompat

# import maya.cmds as cmds
# import maya.OpenMaya as om
# import maya.OpenMayaUI as omui
from core import VideoProcessor


class ReferenceImporterDialog(QDialog):
    _ui_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "ui", "main_dialog.ui"
    )

    def __init__(self, parent=None) -> None:
        self.ui = QtCompat.loadUi(self._ui_path, self)
        self.setWindowFlags(self.windowFlags())
        self.create_connections()

        self.video_processor = VideoProcessor()

        super(ReferenceImporterDialog, self).__init__(parent)

    def create_connections(self):
        (
            self.ui
            .pushButton_fileExplorer_input
            .clicked
            .connect(self.set_input)
        )
        (
            self.ui
            .pushButton_fileExplorer_output
            .clicked
            .connect(self.set_output)
        )
        (
            self.ui
            .pushButton_create_image_sequence
            .clicked
            .connect(self.create_image_sequence)
        )
        (
            self.ui
            .lineEdit_video_path
            .textChanged
            .connect(self.validate_fields)
        )
        (
            self.ui
            .lineEdit_sequence_file_name
            .textChanged
            .connect(self.validate_fields)
        )
        (
            self.ui
            .lineEdit_start_trim
            .textChanged
            .connect(self.validate_fields)
        )
        (
            self.ui
            .lineEdit_end_trim
            .textChanged
            .connect(self.validate_fields)
        )
        (
            self.ui
            .lineEdit_output_directory
            .textChanged
            .connect(self.validate_fields)
        )

    def set_input(self):
        filename = self.ui.lineEdit_video_path.text()
        selected_filter = "Video File (*.mp4 *.mov *.avi *mkv);;All Files (*.*)"
        input_dialog = QFileDialog(self)
        filename = input_dialog.getOpenFileName(
            self, "Select Video File", filename, selected_filter
        )
        # a tuple is returned where the name of the file is the first item.
        filename = filename[0]

        if filename:
            duration = self.video_processor.get_duration(filename)
            self.ui.lineEdit_end_trim.setText(duration)
            self.ui.lineEdit_video_path.setText(filename)

    def set_output(self):
        try:
            filename = self.ui.lineEdit_output_directory.text()
            output_dialog = QFileDialog(self)
            filename = output_dialog.getExistingDirectory(
                self, "Select Output Path", filename
            )
            if filename[0] != "":
                self.ui.lineEdit_output_directory.setText(filename)
        except Exception as e:
            raise e

    def validate_fields(self):
        """Refactor this to use REGEX for value validation"""
        valid_fields = []
        valid_fields.append(bool(self.ui.lineEdit_video_path.text()))
        valid_fields.append(bool(self.ui.lineEdit_sequence_file_name.text()))
        valid_fields.append(bool(self.ui.lineEdit_start_trim.text()))
        valid_fields.append(bool(self.ui.lineEdit_end_trim.text()))
        valid_fields.append(bool(self.ui.lineEdit_output_directory.text()))

        valid_fields.append(
            self.validate_timecode(self.ui.lineEdit_start_trim.text())
        )
        valid_fields.append(
            self.validate_timecode(self.ui.lineEdit_end_trim.text())
        )

        if all(valid_fields):
            self.ui.pushButton_create_image_sequence.setEnabled(True)
        else:
            self.ui.pushButton_create_image_sequence.setEnabled(False)

    def validate_timecode(self, text):
        timecode_rx = QtCore.QRegExp("([0-9]{2}[:]){1,2}[0-9]{2}[.]?[0-9]+")
        timecode_validator = QtGui.QRegExpValidator(timecode_rx, self)
        state = timecode_validator.validate(text, 0)
        if state[0] == QtGui.QRegExpValidator.Acceptable:
            return True

        else:
            return False

    def create_image_sequence(self):
        try:
            frame_rate = str(self.ui.spinBox_frame_rate.value())

            input_file = os.path.normpath(self.ui.lineEdit_video_path.text())

            trim_start = str(self.ui.lineEdit_start_trim.text())
            trim_end = str(self.ui.lineEdit_end_trim.text())

            output_dir = os.path.normpath(self.ui.lineEdit_output_directory.text())
            output_ext = self.ui.comboBox_file_extension.currentText()

            output_name = (
                self.ui.lineEdit_sequence_file_name.text() + "_%03d" + output_ext
            )
            output_file = os.path.join(output_dir, output_name)

            self.video_processor.create_image_sequence(
                input_file, frame_rate, trim_start, trim_end, output_file
            )

            if self.ui.checkBox_image_plane.isChecked():
                output_file = output_file.replace("%03d", "001")
                image_plane = cmds.imagePlane(fn=output_file)
                cmds.setAttr("%s.useFrameExtension" % image_plane[0], True)
        except Exception as e:
            raise e


def run():
    app = QApplication()
    dialog = ReferenceImporterDialog()
    dialog.show()
    app.exec_()


if __name__ == "__main__":
    run()
