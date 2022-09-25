# server.py
import socket
import threading
import os
from datetime import datetime
import datetime

path = 'logs/log.txt'
pathexists = os.path.exists(path)
if not pathexists:
    os.makedirs('logs')
    a = open(path, 'x')
    a.close()



def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
         
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 9500
ADDRESS = get_ip()
print('My IP is:', ADDRESS+":"+str(PORT))
broadcast_list = []
s.bind((ADDRESS, PORT))


def accept_loop():
    while True:
        s.listen()
        client, client_address = s.accept()
        broadcast_list.append(client)
        start_listenning_thread(client)
        with open('logs/log.txt', 'r') as log:
            history = log.read()
            client.send(history.encode('utf-8'))
        
        
def start_listenning_thread(client):
    client_thread = threading.Thread(
            target=listen_thread,
            args=(client,)
        )
    client_thread.start()
    
    
def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        if message:
            if message == '!.?|list|?.!':
                message = "Online users: "+str(len(broadcast_list))
                print(message)
                broadcast(message)
            else:
                logsize = int(os.path.getsize('logs/log.txt'))
                if logsize >= 67108864:
                    #bytes
                    nowt = datetime.datetime.now()
                    nowti = nowt.strftime('%Y-%m-%d %H-%M-%S')
                    newname = 'logs/'+str(nowti)+'.txt'
                    os.rename('logs/log.txt', newname)
                with open("logs/log.txt", "a+") as log:
                    log.write("\n"+message)
                print(message)
                broadcast(message)
        else:
            print(f"client has been disconnected : {client}")
            return
        
def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
accept_loop()