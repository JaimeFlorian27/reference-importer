import os
import sys
libs =  os.path.abspath(os.path.dirname(__file__)).decode('Cp1252')
libs = os.path.join(libs,'ReferenceImporter\\lib')
sys.path.append(libs)
from PySide2 import QtCore,QtGui,QtWidgets
import maya.cmds as cmds
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
import ReferenceImporter.ui.main_dialog_ui 
reload(ReferenceImporter.ui.main_dialog_ui)
from ReferenceImporter.ui.main_dialog_ui import Ui
import ReferenceImporter.imageSequence 
reload(ReferenceImporter.imageSequence)
from ReferenceImporter.imageSequence import ImageSequencer


def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
class Dialog(QtWidgets.QDialog):

    dlg_instance = None

    @classmethod
    def show_dialog(cls):
        if not cls.dlg_instance:
            cls.dlg_instance = Dialog()

        if cls.dlg_instance.isHidden():
            cls.dlg_instance.show()
        else:
            cls.dlg_instance.raise_()
            cls.dlg_instance.activateWindow()

    def __init__(self,parent=maya_main_window()):
        super(Dialog,self).__init__(parent)
        self.imageSequencer = ImageSequencer()
        self.ui = Ui(self)
        self.CreateConnections()
        self.ui.pushButton_create_image_sequence.setDisabled(True)

    def CreateConnections(self):
        self.ui.pushButton_fileExplorer_input.clicked.connect(self.SetInput)
        self.ui.pushButton_fileExplorer_output.clicked.connect(self.SetOutput)
        self.ui.pushButton_create_image_sequence.clicked.connect(self.CreateImageSequence)

        self.ui.lineEdit.textChanged.connect(self.CheckText)
        self.ui.lineEdit_2.textChanged.connect(self.CheckText)
        self.ui.lineEdit_start_trim.textChanged.connect(self.CheckText)
        self.ui.lineEdit_end_trim.textChanged.connect(self.CheckText)
        self.ui.lineEdit_output_directory.textChanged.connect(self.CheckText)

    def SetInput(self):
        try:
            input_dialog.close()
            input_dialog.deleteLater()
        except:pass
        filename = self.ui.lineEdit.text()
        selected_filter = "Video File (*.mp4 *.mov *.avi *mkv);;All Files (*.*)"
        input_dialog = QtWidgets.QFileDialog(self)
        filename = input_dialog.getOpenFileName(self,"Select Video File", filename,selected_filter)

        if filename[0] != "":
            self.ui.lineEdit.setText(filename[0])
            duration = self.imageSequencer.getDuration(filename[0]).encode('Cp1252')
            print(duration)
            self.ui.lineEdit_end_trim.setText(duration)
    def SetOutput(self):
        try:
            output_dialog.close()
            output_dialog.deleteLater()
        except:pass
        filename = self.ui.lineEdit_output_directory.text()
        output_dialog = QtWidgets.QFileDialog(self)
        output_dialog.setNameFilter('Videos (*.mp4 *.mov *.1)')
        filename = output_dialog.getExistingDirectory(self,"Select Output Pants", filename)
        if filename[0] != "":
            self.ui.lineEdit_output_directory.setText(filename)
    
    def CheckText(self):
        valid_fields = []
        valid_fields.append(bool(self.ui.lineEdit.text()))
        valid_fields.append(bool(self.ui.lineEdit_2.text()))
        valid_fields.append(bool(self.ui.lineEdit_start_trim.text()))
        valid_fields.append(bool(self.ui.lineEdit_end_trim.text()))
        valid_fields.append(bool(self.ui.lineEdit_output_directory.text()))

        valid_fields.append(self.ValidateTimecode(self.ui.lineEdit_start_trim.text()))
        valid_fields.append(self.ValidateTimecode(self.ui.lineEdit_end_trim.text()))

        if all(valid_fields):
            self.ui.pushButton_create_image_sequence.setEnabled(True)
        else : self.ui.pushButton_create_image_sequence.setEnabled(False)

    def ValidateTimecode(self, text, ):
        timecode_rx = QtCore.QRegExp('([0-9]{2}[:]){1,2}[0-9]{2}[.]?[0-9]{0,2}')
        timecode_validator = QtGui.QRegExpValidator(timecode_rx, self)
        state = timecode_validator.validate(text,0)
        if state[0] == QtGui.QRegExpValidator.Acceptable :
            return True

        else : 
            return False

    def CreateImageSequence(self):
        frameRate = str(self.ui.spinBox_frameRate.value())
        print(frameRate)

        input_file = os.path.normpath(self.ui.lineEdit.text())
        print( os.path.normpath(self.ui.lineEdit.text()))

        trim_start = str(self.ui.lineEdit_start_trim.text())
        print(trim_start)
        trim_end = str(self.ui.lineEdit_end_trim.text())
        print(trim_end)

        output_dir = os.path.normpath(self.ui.lineEdit_output_directory.text())
        output_ext = self.ui.comboBox.currentText()
        
        output_name = self.ui.lineEdit_2.text()+"%03d"+output_ext
        output_file = os.path.join(output_dir, output_name)

        print(os.path.join(output_file))

        self.imageSequencer.createSequence(input_file,frameRate,trim_start,trim_end, output_file)
        
        if self.ui.checkBox_imagePlane.isChecked():
            output_file = output_file.replace('%03d', '001')
            image_plane = cmds.imagePlane(fn = output_file)
            cmds.setAttr("%s.useFrameExtension"%image_plane[0],True)