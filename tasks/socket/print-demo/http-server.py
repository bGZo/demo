import socket
import threading
import os

WEBPORT = "."

def handle_client(c, addr):
    print(addr, "connected.")
    with c:
        request = c.recv(1024)

        # parse HTTP headers
        headers = request.split(b'\r\n')
        file = headers[0].split()[1].decode()

        #Load file content
        if file == "/":
            file = "/index.html"

        try:
            with open(WEBPORT + file, 'rb') as f:
                content = f.read()
                response = b"HTTP/1.0 200 OK\r\n\r\n" + content

        except FileNotFoundError:
            response = b"HTTP/1.0 404 Not Found\r\n\r\nFile not found!"

        # send HTTP response
        c.send(response)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 1235))
    s.listen()

    while True:
        c, addr = s.accept()

        t = threading.Thread(target=handle_client, args=(c, addr))
        t.start()
