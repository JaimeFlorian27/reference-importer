
from PySide2 import QtCore,QtGui,QtWidgets
import maya.OpenMaya as om
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from ui import Ui

def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)

class Dialog(QtWidgets.QDialog):
    def __init__(self,parent=maya_main_window()):
        super(Dialog,self).__init__(parent)
        self.ui = Ui().setupUi(self)
    

    
if __name__ == "__main__":
    global dialog
    try:
        dialog.close()
    except:pass

    dialog = Dialog()
    dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
    dialog.show()

