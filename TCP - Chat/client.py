import threading
import socket

# Creating Client
nickname = input('Choose an nickname: ')

# Establishing Connection
host = "127.0.0.1"
port = 5000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            # Handling Messages
            if message == "nickname?":
                client.send(nickname.encode('utf-8'))

            else:
                print(message)

        except:
            print('Your chat connection is closed!')
            client.close()
            break


def send():
    while True:
        message = f'{nickname}: {input("")}'

        if message[len(nickname) + 2:].startswith("/help"):
            print("Here all the available commands:\n"
                  "/quit\n"
                  "/list")

        elif message[len(nickname) + 2:].startswith("/list"):
            client.send(f"LIST".encode('utf-8'))
            online = client.recv(1024).decode("utf-8")

            if len(online) == 1:
                print(online)

            else:
                print(f"clients online :\n".upper())
                print(online)

        elif message[len(nickname) + 2:].startswith("/quit"):
            client.send("QUIT".encode('utf-8'))
            print('Disconnecting!')
            client.close()
            break

        else:
            client.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
