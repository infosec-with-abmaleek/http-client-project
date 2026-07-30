import socket

HOST = "httpbin.org"
PORT = 80

request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {HOST}\r\n"
    "User-Agent: MyHTTPClient/1.0\r\n"
    "Accept: */*\r\n"
    "Connection: close\r\n"
    "\r\n"
)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

client.sendall(request.encode())

response = b""

while True:
    data = client.recv(4096)

    if not data:
        break

    response += data

client.close()

print(response.decode(errors="replace"))