import socket

# function take host and port number and check is given port is opened


def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    is_open = sock.connect_ex((host, port))
    if is_open == 0:
        return True
    else:
        return False


print("scanning port...")

for p in range(0, 10000):
    x = check_port('127.0.0.1', p)
    if x:
        print("port ", p, " is opened")
        print("scanning port...")
