import threading
import socket
import user
from datetime import datetime

SERVER = 'localhost'
PORT = 50000

# Recebe as mensagens
def receiveMessages(client):
    while True:
        msg = client.recv(2048).decode('utf-8')
        print(msg+'\n')

            
# Envia as mensagens para o servidor
def sendMessages(client, username):
    while True:
        msg = input('\n')
        time_now = datetime.now()
        current_time = time_now.strftime("%H:%M")
        client.send(f'{current_time} - "{username}" diz: {msg}'.encode('utf-8'))



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

username = input('Usuário> ')
user_connected = user.User(username)
print('\nCliente conectado!')

# São criadas duas threads. A primeira será responsável por executar a função de recebimento de msgs
# A segunda será responsável por enviar as mensagens.
thread1 = threading.Thread(target=receiveMessages, args=[client])
thread2 = threading.Thread(target=sendMessages, args=[client, user_connected.get_name()])

thread1.start()
thread2.start()

