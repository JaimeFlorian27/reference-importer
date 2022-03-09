import os
import sys
reload(sys)  
sys.setdefaultencoding('Cp1252')
sys.path.append('C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\imageSequence')
sys.path.append('C:\\Users\\Usuario\\OneDrive\\Escritorio\\Arte\\Programación\\Maya\\scripts\\imageSequence\\ReferenceImporter\\lib')
sys.path.append('C:\\Python27\\Lib\\site-packages')
from PySide2 import QtCore,QtGui,QtWidgets
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
    
    def CreateConnections(self):
        self.ui.pushButton_fileExplorer_input.clicked.connect(self.SetInput)
        self.ui.pushButton_fileExplorer_output.clicked.connect(self.SetOutput)
        self.ui.pushButton_create_image_sequence.clicked.connect(self.CreateImageSequence)
    def SetInput(self):
        try:
            input_dialog.close()
            input_dialog.deleteLater()
        except:pass
        input_dialog = QtWidgets.QFileDialog(self)
        #input_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        input_dialog.setNameFilter('Videos (*.mp4 *.mov *.1)')
        filename = input_dialog.getOpenFileName()
        self.ui.lineEdit.setText(filename[0])
        '''if input_dialog.exec_():
            filename = input_dialog.selectedFiles()
            self.ui.lineEdit.setText(filename[0])
            print(filename)'''
    def SetOutput(self):
        try:
            output_dialog.close()
            output_dialog.deleteLater()
        except:pass
        output_dialog = QtWidgets.QFileDialog(self)
        #output_dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        output_dialog.setNameFilter('Videos (*.mp4 *.mov *.1)')
        filename = output_dialog.getExistingDirectory()
        self.ui.lineEdit_output_directory.setText(filename)
    def CreateImageSequence(self):
        self.imageSequencer.video_file = os.path.normpath(self.ui.lineEdit.text())
        print(whatisthis(self.imageSequencer.video_file))
        self.imageSequencer.output_dir =  os.path.normpath(self.ui.lineEdit_output_directory.text())
        print(whatisthis(self.imageSequencer.output_dir))
        self.imageSequencer.createSequence()
        

def whatisthis(s):
    if isinstance(s, str):
        print ("ordinary string")
    elif isinstance(s, unicode):
        print ("unicode string")
    else:
        print ("not a string")


if __name__ == "__main__":
    global dialog
    try:
        dialog.close()
    except:pass
    dialog = Dialog()
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.show()