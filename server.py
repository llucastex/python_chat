import threading
import socket

SERVER = 'localhost'
PORT = 50000

# Funçao principal que recebe as mensagens e faz o broadcast
def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break

# Função que fará a transmissão da msg para todos da rede
def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)

# Deleta um cliente
def deleteClient(client):
    clients.remove(client)

clients = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criamos um socket de entrada aguardando um cliente
server.bind((SERVER, PORT)) # associamos o numero de porta do servidor ao socket
server.listen() # assim o socket de entrada esta criado e escutando requisições TCP do cliente.
print('Servidor inicializado!')
print('----------------------')


while True:
    client, addr = server.accept() # quando um cliente bate a porta, é criado um novo socket, chamado client,
    # dedicado a esse cliente em específico.
    print("Cliente se conectou com a porta: " + str(addr[1]))
    clients.append(client)

    # Inicia a thread do servidor
    thread = threading.Thread(target=messagesTreatment, args=[client])
    thread.start()

