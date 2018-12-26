from jim.server import JSONResponse


def echo_controller(request):

    return JSONResponse(200, 'echo', request.body)
