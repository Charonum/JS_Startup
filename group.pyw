import threading
from tkinter import *
import os
import socket
from tkinter import messagebox


os.system("TASKKILL /F /IM cmd.exe")


class GUI:
    client_socket = None
    last_received_message = None

    def __init__(self, master, serverid):
        f = open("Logged.txt", "r")
        self.username = f.read()
        self.serverid = serverid
        f.close()
        self.username = self.username.replace(".cacc", "")
        self.root = master
        self.chat_transcript_area = None
        self.enter_text_widget = None
        self.initialize_socket()
        self.initialize_gui()
        self.listen_for_incoming_messages_in_a_thread()

    def initialize_socket(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_ip = '50.113.72.248'
        remote_port = 25565
        self.client_socket.connect((remote_ip, remote_port))

    def initialize_gui(self):
        self.root.title("CharonChat")
        self.root.iconbitmap("CC logo.ico")
        self.root.resizable(0, 0)
        self.display_chat_box()
        self.on_join()
        self.display_chat_entry_box()

    def listen_for_incoming_messages_in_a_thread(self):
        thread = threading.Thread(target=self.receive_message_from_server, args=(self.client_socket,))
        thread.start()

    def receive_message_from_server(self, so):
        while True:
            buffer = so.recv(256)
            if not buffer:
                break
            message = buffer.decode('utf-8')
            if f"id={self.serverid}" in message:
                self.chat_transcript_area.insert('end', str(message).replace(f"id={self.serverid}", "") + '\n')
                self.chat_transcript_area.yview(END)
            elif "@logserverusage@" in message:
                pass
            else:
                pass

        so.close()

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

    def on_join(self):
        self.client_socket.send((self.username + f" has joinedid={self.serverid}").encode('utf-8'))

    def on_enter_key_pressed(self, event):
        self.send_chat()
        self.clear_text()

    def clear_text(self):
        self.enter_text_widget.delete(1.0, 'end')

    def send_chat(self):
        senders_name = self.username + ": "
        data = (self.enter_text_widget.get(1.0, 'end').strip() + f"id={self.serverid}")
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8').replace(f"id={self.serverid}", "") + '\n')
        self.chat_transcript_area.yview(END)
        self.client_socket.send(message)
        self.enter_text_widget.delete(1.0, 'end')
        return 'break'

    def on_close_window(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            import os
            self.client_socket.send((self.username + " has left").encode("utf-8"))
            self.root.destroy()
            self.client_socket.close()
            os.system("ServerSelect.pyw")
            exit(0)


if __name__ == '__main__':
    def start(id__):
        if messagebox.askokcancel("Warning", "There seems to be a delay from your PC to the server. Delay: 8.9s\nDo you still want to join?"):
            id__ = id__.get()
            root.destroy()
            root2 = Tk()
            gui = GUI(root2, id__)
            root2.protocol("WM_DELETE_WINDOW", gui.on_close_window)
            root2.mainloop()
    root = Tk()
    root.title("Group Chat")
    root.iconbitmap("CC logo.ico")
    root.geometry("250x300")
    Label(root, text="Server Id:").pack()
    id_ = Entry(root, width=20)
    id_.pack()
    Button(root, text="Join", command=lambda: start(id_)).pack()
    root.mainloop()
