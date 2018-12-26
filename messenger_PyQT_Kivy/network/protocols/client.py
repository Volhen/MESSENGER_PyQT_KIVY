import asyncio

from jim.client import JSONResponse, JSONRequest

from network.errors.client import DisconnectError


class SimpleProtocol(asyncio.Protocol):

    __observers = list()


    @classmethod
    def add_observer(cls, observer):

        cls.__observers.append(observer)


    @classmethod
    def remove_observer(cls, observer):

        cls.__observers.remove(observer)
                  

    def send(self, action, data, **headers):

        request = JSONRequest(action, data, **headers)

        self._transport.write(request.to_bytes())


    def connection_made(self, transport):

        self._transport = transport


    def data_received(self, data):

        response = JSONResponse(data) 

        for observer in self.__observers:

            observer.update(response)


    def connection_lost(self, exc):

        raise DisconnectError


class Observer():

    def update(self, response):

        pass
