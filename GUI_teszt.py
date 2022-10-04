import customtkinter
import threading
import datetime
import socket
import PIL
import os


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        name = ["Client v1.1 user"]
        def thread_receiving():
            while True:
                message = s.recv(1024).decode()
                self.Text.configure(state='normal')
                self.Text.insert(customtkinter.END, (message + '\n'))
                self.Text.configure(state='disabled')

        def send():
            message_to_send = self.inputbox.get()
            self.inputbox.delete(0, customtkinter.END)
            if message_to_send == '//list':
                msg = '!.?|list|?.!'
                s.send(msg.encode())
            else:
                now = datetime.datetime.now()
                time = now.strftime("%H:%M:%S")
                msg_with_name = '[' + time + '] ' + '<' + name[0] + '> ' + message_to_send
                s.send(msg_with_name.encode())

        def connect():
            input1 = '192.168.0.45:9500'
            HOST, PORT = input1.split(':')
            s.connect((HOST, int(PORT)))
            thread_receive = threading.Thread(target=thread_receiving)
            thread_receive.start()
            msg = "[Server] " + name[0] + " has joined the chat"
            s.send(msg.encode())


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.title('chat.py client v1.1.0 beta')
        self.columnconfigure(0, weight=1)

        self.Frame_output = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.Frame_output.grid(row=0, column=0, sticky='nesw', padx=20, pady=20)
        self.Frame_output.configure(height=380)
        self.Text = customtkinter.CTkTextbox(master=self.Frame_output, corner_radius=10)
        self.Text.grid(row=0, column=0, sticky='nesw')
        self.Text.configure(width=560, height=380)

        self.Frame_send = customtkinter.CTkFrame(master=self, corner_radius=10)
        self.Frame_send.grid(row=1, column=0, sticky='nesw', padx=20, pady=20)
        self.Frame_send.configure(height=40)
        self.Frame_send.rowconfigure(0, minsize=10)
        self.Frame_send.columnconfigure(0, minsize=5)
        self.Frame_send.rowconfigure(2, minsize=10)
        self.Frame_send.columnconfigure(2, minsize=60)

# -----------------------Message to send-----------------------
        self.inputbox = customtkinter.CTkEntry(master=self.Frame_send)
        self.inputbox.grid(row=1, column=1)
        self.inputbox.configure(width=450)

        self.Button_send = customtkinter.CTkButton(master=self.Frame_send, text='SEND', command=send)
        self.Button_send.grid(row=1, column=3)
        self.Button_send.configure(width=50)




        connect()



if __name__ == '__main__':
    window = Main()
    window.mainloop()
