import threading
import socket

SERVER = 'localhost'
PORT = 50000

clients = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criamos um socket de entrada aguardando um cliente

    try:
        server.bind((SERVER, PORT)) # associamos o numero de porta do servidor ao socket
        server.listen() # assim o socket de entrada esta criado e escutando requisições TCP do cliente.
        print('Servidor inicializado!')
        print('----------------------')
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        client, addr = server.accept() # quando um cliente bate a porta, é criado um novo socket, chamado client,
        # dedicado a esse cliente em específico.
        clients.append(client)

        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break


def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)

main()