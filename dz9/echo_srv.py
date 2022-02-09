import socket
from http import HTTPStatus

PORT = 8888

def get_method(text):
    methods = ['GET', 'POST', 'PUT', 'DELETE',
        'HEAD', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']
    params = text.split(' ')
    if params[0] not in methods:
        method = 'WRONG METHOD'
    else:
        method = params[0]
    http_ver = params[-1]
    if len(params) > 3:
        req = ' '.join(params[1:-1])
    else:
        req = params[1]
    return method, req, http_ver

def resp_status_code(req):
    rstatus = ''
    if '/?status=' in req:
        status_code = req.replace('/?status=', '')
        try:
            status = HTTPStatus(int(status_code))
            rstatus = f'{status.value} {status.name}'
        except ValueError:
            pass

    return rstatus

def prep_answer(data, client):
    lines = data.split('\r\n')
    if len(lines) <= 2:
        return "BAD STATUS\r\n", f"BAD REQUEST: {lines}\r\n"
    method, req, http_ver = get_method(lines[0])
    status = resp_status_code(req)
    if status:
        status_line = f'{http_ver} {status}'
    else:
        status_line = f'{http_ver} 200 OK'
        status = 'Error: Bad Status'
    head = [f'Request Method: {method}',
    f'Request Source: {client}',
    f'Response Status: {status}']
    body = '\r\n'.join(head + lines[2:])
    body_tags = f'<pre>{body}</pre>'
    return status_line, body_tags

print (f'Echo server start on port: {PORT}')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    srv_params = ('', PORT)
    soc.bind(srv_params)
    soc.listen(1)

    while True:
        print('wait connection...')
        conn, client = soc.accept()
        print('connection from', client)

        while True:
            data = conn.recv(1024)
            if not data:
                conn.close()
                break
            print(f'get {len(data)} bytes from client')
            status_line, body = prep_answer(data.decode('utf-8'), client)
            
            print('sending data to client...')
            headers = '\r\n'.join([
                status_line,
                f'Content-Length: {len(body)}',
                'Content-Type: text/html; charset=UTF-8'
            ])
            resp = '\r\n\r\n'.join([
                headers,
                body
            ])
            sent_bytes = conn.send(resp.encode('utf-8'))
            print(f'{sent_bytes} bytes sent')
        conn.close()
