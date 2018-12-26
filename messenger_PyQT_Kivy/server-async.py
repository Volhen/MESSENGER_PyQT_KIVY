import asyncio

from network.protocols.server import SimpleProtocol

import settings


class SimpleServer():

    def __init__(self, protocol=SimpleProtocol):

        self._loop = asyncio.get_event_loop()

        self._protocol = protocol


    def mainloop(self):

        coro = self._loop.create_server(self._protocol, settings.HOST, settings.PORT)

        server = self._loop.run_until_complete(coro)

        try:

            self._loop.run_forever()

        except KeyboardInterrupt:

            pass

        server.close()

        self._loop.run_until_complete(server.wait_closed())

        self._loop.close()


if __name__ == '__main__':

    server = SimpleServer()

    server.mainloop()
