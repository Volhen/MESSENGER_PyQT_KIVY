import sys

from PyQt5 import QtWidgets, QtGui

from guicore.appwindow.body import AppBody

from guicore.appwindow.login import AppLogin

from guicore.appwindow.register import AppRegister

from guicore.appwindow.profile import AppProfile

from guicore.appwindow.adduser import AppAddUser



import settings


class AppWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        
        super(AppWindow, self).__init__()

        self.login = AppLogin()

        self.body = AppBody()

        self.register = AppRegister()

        self.user_profile = AppProfile()

        self.add_user= AppAddUser()

        self.push_button()


    # Обработчик нажатий кнопок 

    def push_button(self):

        # Обработка кнокоп при аутентификации

        self.login.btn_log.clicked.connect(self.push_login)

        self.login.btn_reg.clicked.connect(self.push_register)

        # Обработка кнокоп при регистрации

        self.register.btn_log.clicked.connect(self.push_submit)

        # Обработка кнокоп body (smile, font, menubar)

        self.body.push_button()

        self.body.actionUser_profile.triggered.connect(self.action_user_profile)
        
        self.body.actionAdd_contact.triggered.connect(self.action_add_contact)

        # Обработка при нажатии в User pfofile

        self.user_profile.push_button()

        # Обработка при нажатии в Add user

        self.add_user.btn_ok.clicked.connect(self.add_contact_list)

        self.add_user.btn_cancel.clicked.connect(self.add_user.close)

    
    def add_contact_list(self):
        
        self.add_user.set_DB()

        self.body.show_list_contact_unit()

    def push_login(self):
        
        pas = self.login.setpass.text()

        log = self.login.setlog.text()
        
        if settings.PASSWORD == pas and settings.LOGIN == log:
            
            self.body.show()

            self.login.close()
        
        else:
            
            self.login.setpass.clear()

            self.login.setlog.clear()

    def push_submit(self):

        pas = self.register.setpass.text()

        conf = self.register.setconfirm.text()

        if pas == conf:

            self.body.show()

            self.register.close()

        else:

            self.register.setpass.clear()

            self.register.setconfirm.clear()


    def push_register(self):
        
        self.register.show()

        self.login.close()


    def action_user_profile(self):

        self.user_profile.show()


    def action_add_contact(self):
        
        self.add_user.show()


    def show(self):
        
        # self.login.show()
        self.body.show()
        # self.user_profile.show()



# if __name__ == '__main__':

#     app = QtWidgets.QApplication(sys.argv)

#     form = AppWindow()

#     form.show()

#     sys.exit(app.exec_())
