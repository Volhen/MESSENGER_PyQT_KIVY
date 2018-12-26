from PyQt5 import QtWidgets

from guicore.appwindow.form.register import Ui_MainWindow_Register


class AppRegister(QtWidgets.QMainWindow, Ui_MainWindow_Register):
    
    def __init__(self):
        
        super(AppRegister,self).__init__()

        self.setupUi_register(self)