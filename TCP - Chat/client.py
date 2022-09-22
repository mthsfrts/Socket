import threading
import socket

server_ip = '127.0.0.1'
server_port = 5000

# Creating Client
nickname = input("Choose an nickname: ")
print(f"hey, {nickname} to enter in a chatroom please use the command:".upper(), "/enter")
enter = input()

# Getting Server Details
if enter == "/enter":
    host = input("What is the server ip: ")
    port = input("What is the port: ")

    if host != server_ip and int(port) != server_port:
        print("Connection Error, please check the server details!".upper())

    elif host != server_ip and int(port) == server_port:
        print("Ip Error, please check the server ip!".upper())

    elif host == server_ip and int(port) != server_port:
        print("Port Error, please check the server port!".upper())

    else:
        # Establishing Connection
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, int(port)))


def receive():
    """
    Method responsible to decode and receive client messages.
    """

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
    """
    Method responsible to encode and send client messages.
    """

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
                print(f"clients online :\n".upper(), online)

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
