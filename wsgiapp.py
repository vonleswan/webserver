import os


def app(environ, start_response):
    """A barebones WSGI application.

    This is a starting point for your own Web framework :)
    """
    path = environ['PATH_INFO'].decode()
    file_extention = path[-3:]

    if path == '/index':
        status = '200 OK'
        response_headers = [('Content-Type', 'html')]
        start_response(status, response_headers)
        return [open(os.getcwd() + '/html/index.html', 'r').read()]

    elif file_extention == 'png' or file_extention == 'jpg':
        img = open(os.getcwd() + '/blog' + path, mode='rb').read()
        status = '200 OK'
        response_headers = [('Content-Type', 'image/' + file_extention)]
        start_response(status, response_headers)
        return [img]

    else:
        status = '404 Not Found'
        response_headers = [('Content-Type', 'plaintext/text')]
        start_response(status, response_headers)
        return ['']
