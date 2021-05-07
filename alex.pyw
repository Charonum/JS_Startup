from tkinter import *
from tkinter import messagebox
import random
import os
os.system("TASKKILL /F /IM cmd.exe")

class GUI:
    client_socket = None
    last_received_message = None

    def __init__(self, master):
        f = open("Logged.txt", "r")
        self.username = f.read()
        f.close()
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
        Label(frame, text='Enter message:', font=("Serif", 12)).pack(side='top', anchor='w')
        self.enter_text_widget = Text(frame, width=60, height=3, font=("Serif", 12))
        self.enter_text_widget.pack(side='left', pady=15)
        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)
        frame.pack(side='top')

    def on_enter_key_pressed(self, event):
        self.send_chat()
        self.clear_text()

    def clear_text(self):
        self.enter_text_widget.delete(1.0, 'end')

    def send_chat(self):
        senders_name = self.username + ": "
        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (senders_name + data)
        self.chat_transcript_area.insert('end', message + '\n')
        self.chat_transcript_area.yview(END)
        if "?" in data:
            listt = ["idk", "huh", "idk", "idk", "idk"]
            message = "A.L.E.X.: " + random.choice(listt)
            self.chat_transcript_area.insert('end', message + '\n')
            self.chat_transcript_area.yview(END)
        elif "when" in data:
            listt = ["idk", "huh", "idk", "idk", "idk"]
            message = "A.L.E.X.: " + random.choice(listt)
            self.chat_transcript_area.insert('end', message + '\n')
            self.chat_transcript_area.yview(END)
        elif "where" in data:
            listt = ["idk", "huh", "idk", "idk", "idk"]
            message = "A.L.E.X.: " + random.choice(listt)
            self.chat_transcript_area.insert('end', message + '\n')
            self.chat_transcript_area.yview(END)
        elif "how" in data:
            listt = ["idk", "huh", "idk", "idk", "idk"]
            message = "A.L.E.X.: " + random.choice(listt)
            self.chat_transcript_area.insert('end', message + '\n')
            self.chat_transcript_area.yview(END)
        elif "what" in data:
            listt = ["idk", "huh", "idk", "idk", "idk"]
            message = "A.L.E.X.: " + random.choice(listt)
            self.chat_transcript_area.insert('end', message + '\n')
            self.chat_transcript_area.yview(END)
        elif "who" in data:
            listt = ["idk", "huh", "idk", "idk", "idk"]
            message = "A.L.E.X.: " + random.choice(listt)
            self.chat_transcript_area.insert('end', message + '\n')
            self.chat_transcript_area.yview(END)
        elif "which" in data:
            listt = ["idk", "huh", "idk", "idk", "idk"]
            message = "A.L.E.X.: " + random.choice(listt)
            self.chat_transcript_area.insert('end', message + '\n')
            self.chat_transcript_area.yview(END)
        elif "why" in data:
            listt = ["idk", "huh", "idk", "idk", "idk"]
            message = "A.L.E.X.: " + random.choice(listt)
            self.chat_transcript_area.insert('end', message + '\n')
            self.chat_transcript_area.yview(END)
        else:
            self.chat_transcript_area.insert('end', "A.L.E.X.: K" + '\n')
            self.chat_transcript_area.yview(END)
        self.enter_text_widget.delete(1.0, 'end')
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
username = username.replace(".cacc", "")
root2 = Tk()
gui = GUI(root2)
root2.protocol("WM_DELETE_WINDOW", gui.on_close_window)
root2.mainloop()
