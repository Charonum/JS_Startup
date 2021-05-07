from tkinter import *
from tkinter import messagebox
import os
os.system("TASKKILL /F /IM cmd.exe")

class GUI:
    client_socket = None
    last_received_message = None

    def __init__(self, master):
        f = open("Logged.txt", "r")
        self.username = f.read()
        f.close()
        self.username = self.username.replace(".cacc", "")
        self.root = master
        self.chat_transcript_area = None
        self.enter_text_widget = None
        self.initialize_gui()

    def initialize_gui(self):
        self.root.title("JS")
        self.root.iconbitmap("JS logo.ico")
        self.root.resizable(0, 0)
        self.display_chat_box()
        self.display_chat_entry_box()


    def display_chat_box(self):
        frame = Frame()
        Label(frame, text='Chat Box:', font=("Serif", 12)).pack(side='top', anchor='w')
        self.chat_transcript_area = Text(frame, width=60, height=10, font=("Serif", 12))
        scrollbar = Scrollbar(frame, command=self.chat_transcript_area.yview, orient=VERTICAL)
        self.chat_transcript_area.config(yscrollcommand=scrollbar.set)
        self.chat_transcript_area.bind('<KeyPress>', lambda e: 'break')
        self.chat_transcript_area.pack(side='left', padx=10)
        scrollbar.pack(side='right', fill='y')
        frame.pack(side='top')

    def display_chat_entry_box(self):
        frame = Frame()

        def lel():
            self.on_enter_key_pressed()

        Label(frame, text='Enter message:', font=("Serif", 12)).pack(side='top', anchor='w')
        self.yo_button = Button(frame, text="Got any quests?", command=lel).pack()
        frame.pack(side='top')

    def on_enter_key_pressed(self):
        self.send_chat()

    def send_chat(self):
        senders_name = self.username + ": "
        data = "Got any quests?"
        message = (senders_name + data)
        self.chat_transcript_area.insert('end', message + '\n')
        self.chat_transcript_area.yview(END)
        if data == "Got any quests?":
            self.chat_transcript_area.insert('end', 'Charump: Yeah! Say this to someone: "hey u so fat", you get admin for 5 min!' + '\n')
            self.chat_transcript_area.yview(END)
        else:
            self.chat_transcript_area.insert('end', "A.L.E.X.: K" + '\n')
            self.chat_transcript_area.yview(END)
        return 'break'

    def on_close_window(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            import os
            self.root.destroy()
            os.system("ServerSelect.pyw")
            exit(0)


f = open("Logged.txt", "r")
user = f.read()
f.close()
username = user
root2 = Tk()
gui = GUI(root2)
root2.protocol("WM_DELETE_WINDOW", gui.on_close_window)
root2.mainloop()