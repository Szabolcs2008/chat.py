def program():
    namefile = open('name.txt', 'a+')
    namefile.close()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        input1 = input('Host IP + port (ex.: 0.0.0.0:25565): ')
        inputs = input1.split(':')
        host, port = inputs[0], int(inputs[1])
    except:
        host = 0
        port = 0
        print('Invalid IP or port')
        exit()

    s.connect((host, port))

    namefile = open('name.txt', 'r')
    prevname = namefile.read()
    namefile.close()
    useprevname = input('Use previous name? (y/n)' + '(' + prevname + ')')
    if useprevname in ('n', 'N'):
        os.remove('name.txt')
        with open('name.txt', 'a+') as namefile:
            name = input('Username: ')
            namefile.write(name)
    if useprevname in ('y', 'Y'):
        with open('name.txt', 'r') as namefile:
            name = namefile.read()

    msg = "[Server] " + name + " has joined the chat"
    s.send(msg.encode())
    msg = ""

    def thread_sending():
        while True:
            message_to_send = input()
            if message_to_send == '//list':
                msg = '!.?|list|?.!'
                s.send(msg.encode())
            else:
                msg_with_name = '<' + name + '> ' + message_to_send
                s.send(msg_with_name.encode())

    def thread_receiving():
        while True:
            message = s.recv(1024).decode()
            print(message)


    thread_send = threading.Thread(target=thread_sending)
    thread_receive = threading.Thread(target=thread_receiving)
    thread_send.start()
    thread_receive.start()


