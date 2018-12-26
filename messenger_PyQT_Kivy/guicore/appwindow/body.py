from PyQt5 import QtWidgets

from guicore.appwindow.form.body_mes import Ui_MainWindow_Body

from DB.use_db import UseDatabase

    
class AppBody(QtWidgets.QMainWindow, Ui_MainWindow_Body):
    
    def __init__(self):
        
        super(AppBody,self).__init__()

        self.setupUi_body(self)

        self._db = UseDatabase()

        self.show_list_contact_all()


    def show_list_contact_unit(self):
        
        list_contact = self._db.return_list_name()

        count = int(len(list_contact))

        itm = list_contact.pop()

        self.display_list.append('{}{}'.format(count,'. ') + itm)


    def show_list_contact_all(self):
        
        list_contact = self._db.return_list_name() 

        for index, value in enumerate(list_contact,start=1):

            self.display_list.append('{}{}'.format(index,'. ') + value)
        
    
    def push_button(self):

        # Обработка для отображения смайлов

        self.btn_smile_1.clicked.connect(self.action_smile_1)

        self.btn_smile_2.clicked.connect(self.action_smile_2)

        self.btn_smile_3.clicked.connect(self.action_smile_3)

        # Обработка при смены фона текста

        self.btn_bold.clicked.connect(self.action_bold)

        self.btn_italic.clicked.connect(self.action_italic)

        self.btn_underlined.clicked.connect(self.action_underlined)
    

     # *************************action fon text*************************  
    def action_bold(self):
        
        cursor = self.input.textCursor()

        text = cursor.selectedText()

        self.input.insertHtml('<b>%s<b/>' % text)

    
    def action_italic(self):
        
        cursor = self.input.textCursor()

        text = cursor.selectedText()

        self.input.insertHtml('<i>%s<i/>' % text)


    def action_underlined(self):
        
        cursor = self.input.textCursor()

        text = cursor.selectedText()

        self.input.insertHtml('<u>%s<u/>' % text)

    # *************************action smile in text*************************
    def action_smile_1(self):

        self.input.insertHtml('<img src="src/smile/ab.gif"/>')


    def action_smile_2(self):

        self.input.insertHtml('<img src="src/smile/ac.gif"/>')


    def action_smile_3(self):

        self.input.insertHtml('<img src="src/smile/ai.gif"/>')