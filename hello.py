def application(environ, start_response):
    status = '200 OK'
    headers = [
            ('Content-Type', 'text/plain')
            ]
d = parse_qs(environ['QUERY_STRING'])

start_response(status, headers )
# return [ body ]

body = []
for key, value in d:
    body.append(key " = " + value)
