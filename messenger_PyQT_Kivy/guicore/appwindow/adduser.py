from PyQt5 import QtWidgets

from guicore.appwindow.form.add_user import Ui_MainWindow_Add

from DB.use_db import UseDatabase

    
class AppAddUser(QtWidgets.QMainWindow, Ui_MainWindow_Add):
    
    def __init__(self):
        
        super(AppAddUser,self).__init__()

        self.setupUi_add_user(self)
        
        self._DB = UseDatabase()

    def set_DB(self):

        self._DB.add_user(self.input_name.text(),self.input_log.text(), self.input_email.text())
        
        self.input_name.clear()

        self.input_log.clear()

        self.input_email.clear()

        self.close()

    # def push_button(self):
    
    #     self.btn_ok.clicked.connect(self.set_DB)

    #     self.btn_cancel.clicked.connect(self.close)