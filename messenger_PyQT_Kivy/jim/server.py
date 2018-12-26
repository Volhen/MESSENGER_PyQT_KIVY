from network.jim.server import JSONResponse, JSONRequest

from utility import compressed, decompressed


class JSONRequest(JSONRequest):

    @decompressed
    def __init__(self, message_bytes):

        return super(JSONRequest, self).__init__(message_bytes)


class JSONResponse(JSONResponse):

    @compressed
    def to_bytes(self):

        return super(JSONResponse, self).to_bytes()
