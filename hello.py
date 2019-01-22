bind = '127.0.0.1:8000'
workers = 2
def app(environ, start_response):
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
            ]
    # d = parse_qs(environ['QUERY_STRING'])

    # body = []
    # for key, value in d:
    #     body.append(key " = " + value)

    body = "\n".join(environ.get('QUERY_STRING').split("&"))
    start_response(status, headers )
    # return [ body ]


return body
