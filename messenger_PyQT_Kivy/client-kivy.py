import sys

import socket

from threading import Thread

from jim.client import JSONRequest, JSONResponse

from guicore.appkivy.mainapp import MainApp

from guicore.appkivy.mainapp import ContainerWidget

# mainapp import MainApp

# from mainapp import ContainerWidget

import settings


class MainApp (MainApp):

    def __init__(self, *args, **kwargs):

        super(MainApp, self).__init__(*args, **kwargs)

        # Создаем экземпляр сокет соединения
        self._sock = socket.socket()

        # Связываем сокет соединение с хостом и портом сервера 
        self._sock.connect((settings.HOST, settings.PORT))

    
    def build(self):
        
        self.container = ContainerWidget()

        self.work_process()

        return self.container


    def read(self):
        
        while True:

            # Получаем данные с сервера
            bytes_data = self._sock.recv(settings.BUFFER_SIZE)

            # Приводим полученные данные к строковому виду
            response = JSONResponse(bytes_data)

            # Выводим полученные данные на экран

            self.container.display_set(response.body)

    def write(self,instance):

        # Вводим данные с клавиатуры
        
        str_data = self.container.ids.input.text

        # Приводим отправляемые данные к байтовому виду
        request = JSONRequest(202,'echo',str_data)

        # Преобразовываем JSON в байты
        bytes_data = request.to_bytes()

        # Отправляем данные на сервер
        
        self._sock.send(bytes_data)

        # Отчищаем строку

        self.container.clear()

    
    def work_process(self):

        self.container.ids.btn.bind(on_press = self.write)
                
        display_thread = Thread(target=self.read, daemon=True)
        
        display_thread.start()

if __name__ == '__main__':

    client = MainApp()

    client.run()
