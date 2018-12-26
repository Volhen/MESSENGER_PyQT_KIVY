import asyncio

import actions.server as actions

from network.errors.server import ForbiddenError

from jim.server import JSONRequest, JSONResponse


class SimpleProtocol(asyncio.Protocol):

    __clients = list()


    def connection_made(self, transport):

        print(transport)

        if not transport in self.__clients:

            self.__clients.append(transport)

        self._transport = transport


    def handle_request(self, request):

        if not request.action in actions.actions_list:

            return JSONResponse(404, request.action, 'Not supported action.')

        controller = actions.actions_list.get(request.action)

        response = controller(request)

        headers = dict(request.headers)

        if 'broadcast' in headers:

            for client in self.__clients:

                if not client is self._transport:

                    client.write(response.to_bytes())

        return response


    def data_received(self, data):

        request = JSONRequest(data)

        try:

            response = self.handle_request(request)

        except ForbiddenError as err:

            response = JSONResponse(403, request.action, err)

        except Exception as err:

            response = JSONResponse(500, request.action, err)

        self._transport.write(response.to_bytes())


    def connection_lost(self, exc):

        self.__clients.remove(self._transport)

        self._transport.close()
