def application(environ, start_response):
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
            ]
    # d = parse_qs(environ['QUERY_STRING'])

    # body = []
    # for key, value in d:
    #     body.append(key " = " + value)

    body = "\r\n".join(environ['QUERY_STRING'].split("&"))
    start_response(status, headers )
    # return [ body ]


return body
