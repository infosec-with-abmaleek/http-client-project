import socket

HOST = "example.com"
PORT = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[+] Connecting...")

client.connect((HOST, PORT))

print(f"[+] Connected to {HOST}:{PORT}")

client.close()

print("[+] Connection closed")