Keylogger Botnet
Overview
This repository contains a keylogger botnet implementation for educational purposes. The tool demonstrates basic functionality for capturing and transmitting keystrokes from a client (bot) to a server (C2 server). The keylogger captures keystrokes on the client machine and sends them to the server, which logs them into a text file.

Important: This tool is intended for educational purposes only. Unauthorized use of keyloggers or similar tools for capturing user input without consent is illegal and unethical. The creator and contributors of this tool are not responsible for any misuse or illegal activities performed with this code.

Components
Client Script: Captures keystrokes on the client machine and sends them to the server.
Server Script: Receives and logs keystrokes sent by the client into a text file.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/yourusername/keylogger-botnet.git
cd keylogger-botnet
Install Required Libraries:

The scripts use pynput for keystroke capture. Install it using pip:

bash
Copy code
pip install pynput
Usage
Server
Run the Server Script:

On the host machine where you want to receive and log keystrokes, run the server script:

bash
Copy code
python server.py
The server will start listening for connections and log received data into keystrokes.txt.

Client
Configure the Client Script:

Edit the client.py script to specify the correct IP address and port of the server:

python
Copy code
SERVER_HOST = ""  # Replace with your server's IP address
SERVER_PORT = 9999
Run the Client Script:

On the client machine where you want to capture keystrokes, run the client script:

bash
Copy code
python client.py
The client will connect to the server, capture keystrokes, and send them to the server. Press esc to stop the keystroke capture.

Example
Test Message: The client script sends a test message to the server upon connection.
Keystroke Collection: Keystrokes are collected and sent to the server, which logs them into keystrokes.txt.
Ethical Considerations
Warning: This tool is for educational purposes only. Using keyloggers or any other tools to capture user input without explicit consent is illegal and unethical. The creators and contributors of this repository are not responsible for any misuse or illegal activities performed with this code. Use this tool responsibly and within the boundaries of the law.

Contact
For any questions or issues, please open an issue on the GitHub repository.
