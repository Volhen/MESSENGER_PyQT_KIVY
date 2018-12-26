from PyQt5 import QtWidgets

from guicore.appwindow.form.login import Ui_MainWindow_Login


class AppLogin(QtWidgets.QMainWindow, Ui_MainWindow_Login):
    
    def __init__(self):
        
        super(AppLogin,self).__init__()

        self.setupUi_login(self)
    
    