import socket
import sys

if len(sys.argv) < 3:
    print('client.py hostname port')
    sys.exit()

argv = sys.argv
host = argv[1]
port = argv[2]

# host = "130.37.198.89"
# port = 5378

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

alias = ''

try:
    socket.connect((host, port))
except socket.error as e:
    print(str(e))
    sys.exit()


def send_message(outgoing_socket, outgoing_message):
    try:
        outgoing_socket.send(bytes(outgoing_message, 'UTF-8'))
    except socket.error as e:
        print(str(e))
        sys.exit()


def receive_message(sock):
    try:
        message_received = sock.recv(1024)
        print("Incoming msg: {}\n".format(message_received))

    except socket.error as e:
        print(str(e))
        sys.exit()


while len(alias) < 3:
    alias = input("Insert your name (more than 3 characters)\n")

sentence = "HELLO-FROM {}\n".format(alias)
send_message(socket, sentence)
receive_message(socket)

while True:

    message = input('users, @, !exit\n')

    if message == "users":
        data = "WHO\n"
        send_message(socket, data)
    elif message == '!exit':
        print('closing ...')
        break
    elif message.startswith('@'):
        whisper = message.replace('@', 'SEND ')
        data = "{}\n".format(whisper)
        send_message(socket, data)

    receive_message(socket)
socket.close()
print("Connection lost")
