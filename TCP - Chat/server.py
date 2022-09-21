import threading
import socket

# Creating Server
host = "127.0.0.1"
port = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)

# Creating Dictionary
clients = []
nicknames = []


def broadcast(message, client):
    """
    Responsible to broadcast clients message through the chatroom
    """
    for c in clients:
        if c != client:
            c.send(message)


def handle_client(client):
    """
    Function responsible to handle clients connections
    """
    while True:
        try:
            # getting clients message
            check = message = client.recv(1024)

            # checking clients message for commands
            if check.decode("utf-8").startswith("QUIT"):
                index = clients.index(client)  # getting the index of the particular client
                clients.remove(client)  # removing in case of an error
                nickname = nicknames[index]  # bind the nickname to the client by index
                broadcast(f'{nickname} has left the chat!'.encode('utf-8').upper(), client)  # broadcasting the close connection
                print(f'{nickname} has left the server!')  # Terminal return close client connection
                nicknames.remove(nickname)  # removing nickname
                client.close()  # closing client connection
                continue

            elif check.decode("utf-8").startswith("LIST"):

                if len(nicknames) == 1:
                    client.send("Your are the only client in the chat!".upper().encode("utf-8"))

                else:
                    client.send(f"{nicknames}".encode("utf-8"))
                continue

            else:
                broadcast(message, client)  # broadcasting messages

        except:
            break


def main_receive():
    """
    Function responsible to receive the clients connections
    """
    while True:
        try:
            # Server Status
            print("Server is running and listening ...")

            # starting the accept method and splitting the details into clients and addresses
            client, address = sock.accept()

            # Server Terminal Return
            print(f"Connection is established with {str(address)}!".title())

            # Getting nickname
            client.send("nickname?".encode("utf-8"))
            nickname = client.recv(1024).decode("utf-8")

            # Server Terminal Details Return
            print(f"The nickname of this client is {nickname}".encode('utf-8'))

            # Greeting the Client
            client.send("You are connected!\n".encode("utf-8").upper())
            client.send(f"Welcome to the chat, {nickname}!".encode("utf-8").upper())

            # Populating lists
            nicknames.append(nickname)
            clients.append(client)

            # Broadcast New Connection
            broadcast(f'{nickname} has connected.'.encode('utf-8').upper(), client)

            # Starting Threads
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()

        except KeyboardInterrupt:
            print(f"\nINFO: KeyboardInterrupt".upper())
            print("Closing all sockets and exiting chat server...".upper())
            sock.close()
            exit(0)


if __name__ == "__main__":
    main_receive()
