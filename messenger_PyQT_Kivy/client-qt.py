import sys

import socket

from threading import Thread

# from network.socket.client import EchoClient

from jim.client import JSONRequest, JSONResponse

from PyQt5 import QtWidgets

from guicore.appwindow.appwindow import AppWindow

import settings


class EchoClient (AppWindow):

    def __init__(self):

        super(EchoClient, self).__init__()

        # Создаем экземпляр сокет соединения
        self._sock = socket.socket()

        # Связываем сокет соединение с хостом и портом сервера 
        self._sock.connect((settings.HOST, settings.PORT))

    def read(self):
        
        while True:

            # Получаем данные с сервера
            bytes_data = self._sock.recv(settings.BUFFER_SIZE)

            # Приводим полученные данные к строковому виду
            response = JSONResponse(bytes_data)

            # Выводим полученные данные на экран
            
            self.body.display.append(response.body)

    def write(self):

        # Вводим данные с клавиатуры
        
        str_data = self.body.input.toHtml()

        # Приводим отправляемые данные к байтовому виду
        request = JSONRequest(202,'echo',str_data)

        # Преобразовываем JSON в байты
        bytes_data = request.to_bytes()

        # Отправляем данные на сервер
        
        self._sock.send(bytes_data)

        self.body.input.clear()

    
    def run(self):
        
        self.body.btn.clicked.connect(self.write)
                
        display_thread = Thread(target=self.read, daemon=True)
        
        display_thread.start()

        self.show()


if __name__ == '__main__':

    
    app = QtWidgets.QApplication(sys.argv)

    client = EchoClient()

    client.run()

    sys.exit(app.exec_())
