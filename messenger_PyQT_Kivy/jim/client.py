from network.jim.client import JSONResponse, JSONRequest

from utility import compressed, decompressed


class JSONResponse(JSONResponse):

    @decompressed
    def __init__(self, message_bytes):

        return super(JSONResponse, self).__init__(message_bytes)


class JSONRequest(JSONRequest):

    @compressed
    def to_bytes(self):

        return super(JSONRequest, self).to_bytes()
