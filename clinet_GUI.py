# client.py
import socket
import datetime
import threading
import tkinter
from tkinter import *
from tkinter.ttk import *
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = []

def connect():
    input1 = entry_address.get()
    HOST, PORT = input1.split(':')
    s.connect((HOST, int(PORT)))
    thread_receive = threading.Thread(target=thread_receiving)
    thread_receive.start()
    msg = "[Server] " + name[0] + " has joined the chat"
    s.send(msg.encode())
    entry_address.delete(0, END)
    entry_address.destroy()
    label2.destroy()
    button_connect.destroy()
    entry.configure(state='normal')
    button.configure(state='normal')


def send():
    message_to_send = entry.get()
    entry.delete(0, END)
    if message_to_send == '//list':
        msg = '!.?|list|?.!'
        s.send(msg.encode())
    else:
        now = datetime.datetime.now()
        time = now.strftime("%H:%M:%S")
        msg_with_name = '[' + time + '] ' + '<' + name[0] + '> ' + message_to_send
        s.send(msg_with_name.encode())


def thread_receiving():
    while True:
        message = s.recv(1024).decode()
        t.configure(state='normal')
        t.insert(END, (message+'\n'))
        t.configure(state='disabled')


def add():
    t.configure(state='normal')
    ins = str(entry.get()) + "\n"
    t.insert(END, ins)
    entry.delete(0, END)
    t.configure(state='disabled')


def set_name(n=name):
    n.append(str(entry_name.get()))
    entry_name.configure(state='disabled')
    entry_address.configure(state='normal')
    button_connect.configure(state='normal')
    name_button.configure(state='disabled')


root = Tk()
main_frame = tkinter.Frame(root)
main_frame.pack(side=TOP)
name_frame = tkinter.Frame(main_frame)
name_frame.pack(side=TOP)
label1 = tkinter.Label(master=name_frame, text='Username:')
label1.pack(side=LEFT)
entry_name = tkinter.Entry(master=name_frame)
entry_name.pack(side=LEFT)
name_button = tkinter.Button(master=name_frame, command=set_name, text='Select name')
name_button.pack(side=LEFT)

textbox_frame = tkinter.Frame()
textbox_frame.pack(side=TOP, pady=10)

input_frame = tkinter.Frame()
input_frame.pack(side=BOTTOM)

addr_frame = tkinter.Frame(master=main_frame)
addr_frame.pack(side=TOP)
label2 = tkinter.Label(text='Host:', master=addr_frame)
label2.pack(side=LEFT)
entry_address = tkinter.Entry(master=addr_frame)
entry_address.pack(side=LEFT)
button_connect = tkinter.Button(text='Connect', master=addr_frame, command=connect)
button_connect.pack(side=RIGHT)
entry_address.configure(state='disabled')
button_connect.configure(state='disabled')


entry = tkinter.Entry(width=100, master=input_frame)
entry.pack(side=LEFT)
entry.configure(state='disabled')
button = tkinter.Button(text='Send', command=send, master=input_frame,)
button.pack(side=RIGHT)
button.configure(state='disabled')
horizontal = Scrollbar(textbox_frame,
                       orient='horizontal')
horizontal.pack(side=BOTTOM,
                fill=X)
vertical = Scrollbar(textbox_frame)
vertical.pack(side=RIGHT,
              fill=Y)

t = Text(width=90, height=35,
         master=textbox_frame,
         xscrollcommand=horizontal.set,
         yscrollcommand=vertical.set, )
t.pack(side=TOP,
       fill=X)
t.configure(state='disabled')

horizontal.config(command=t.xview)
vertical.config(command=t.yview)
root.mainloop()