import customtkinter


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()
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

        self.Button_send = customtkinter.CTkButton(master=self.Frame_send, text='SEND')
        self.Button_send.grid(row=1, column=3)
        self.Button_send.configure(width=50)


if __name__ == '__main__':
    window = Main()
    window.mainloop()
