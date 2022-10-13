import threading
import socket
import user
from datetime import datetime

SERVER = 'localhost'
PORT = 50000


def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # try:
    client.connect((SERVER, PORT))
    # except:
        # return print('\nNão foi possívvel se conectar ao servidor!\n')

    username = input('Usuário> ')
    user_connected = user.User(username)
    print('\nCliente conectado!')

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, user_connected.get_name()])

    thread1.start()
    thread2.start()


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            # time_now = datetime.now()
            # current_time = time_now.strftime("%H:%M:%S")
            # print(current_time +' - '+msg+'\n')
            print(msg+'\n')
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break
            

def sendMessages(client, username):
    while True:
        try:
            msg = input('\n')
            time_now = datetime.now()
            current_time = time_now.strftime("%H:%M:%S")
            client.send(f'{current_time} - "{username}" diz: {msg}'.encode('utf-8'))
        except:
            return


main()