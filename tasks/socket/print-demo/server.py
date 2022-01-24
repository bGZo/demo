import socket
import threading

def handle_client(c, addr):
    print(addr, "connected.")
    while True:
        data = c.recv(1024)
        if not data: 
            break
        c.sendall(data)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # AF_INET: ipv4
    # sock_stream: tcp protocol
    s.bind(("0.0.0.0", 1234))
    s.listen()
    # s: listen
    # c: communication
    while True:
        c, addr = s.accept()

        t = threading.Thread(target=handle_client, args=(c, addr))
        t.start()

# multi-thread instead of
# event selectors
# asyncio
