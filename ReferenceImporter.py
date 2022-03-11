import os
import sys
sys.path.append('C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\imageSequence')
sys.path.append('C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\imageSequence\\ReferenceImporter\\lib')
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
        valid = True
        if not self.ui.lineEdit.text(): valid = False 
        if not self.ui.lineEdit_2.text(): valid = False
        if not self.ui.lineEdit_start_trim.text(): valid = False
        if not self.ui.lineEdit_end_trim.text(): valid = False
        if not self.ui.lineEdit_output_directory.text(): valid = False
        self.ui.pushButton_create_image_sequence.setEnabled(valid)

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

        
if __name__ == "__main__":
    global dialog
    try:
        dialog.close()
    except:pass
    dialog = Dialog()
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.show()