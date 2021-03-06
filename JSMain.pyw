import getpass
import shutil
import socket
import threading
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfile

import github
import wget
from github import Github
import os
from HyperlinkManager import HyperlinkManager

os.system("TASKKILL /F /IM cmd.exe")


def login():
    f = open("Logged.txt", "r")
    user = f.read()
    if user == "":
        pass
    else:
        global username
        username = user
        root2 = Tk()
        gui = GUI(root2)
        root2.protocol("WM_DELETE_WINDOW", gui.on_close_window)
        root2.mainloop()
    import os

    def delete3():
        screen4.destroy()

    def delete4():
        screen5.destroy()

    def password_not_recognised():
        global screen4
        screen4 = Toplevel(screen)
        screen4.title("Error")
        screen4.geometry("150x100")
        screen4.iconbitmap('CC logo.ico')
        Label(screen4, text="Password Error").pack()
        Button(screen4, text="OK", command=delete3).pack()

    def user_not_found():
        global screen5
        screen5 = Toplevel(screen)
        screen5.title("Error")
        screen5.geometry("150x100")
        screen5.iconbitmap('CC logo.ico')
        Label(screen5, text="User Not Found").pack()
        Button(screen5, text="OK", command=delete4).pack()

    def register_user():

        username_info = username.get()
        password_info = password.get()
        tfk = open("Token.txt", "r")
        token_ = tfk.read()
        tfk.close()
        g = Github(token_)
        Account_Database = g.get_user().get_repo("AccountData")
        contents = Account_Database.get_contents("")
        for c in contents:
            user_info = username_info + ".cacc"
            if user_info == c.name:
                Label(screen1, text="User Already Exists!", fg="red", font=("calibri", 11)).pack()
                registered = True

        try:
            if registered:
                print("Skipping registration bool")
        except:
            registered = False

        if not registered:
            file = open(username_info + ".cacc", "w")
            file.write(username_info + "\n")
            file.write(password_info)
            file.close()

            username_entry.delete(0, END)
            password_entry.delete(0, END)
            user_file = open(f"{username_info}.cacc", "r")
            user_data = user_file.read()
            Account_Database.create_file(f"{username_info}.cacc", f"{username_info} created an account", user_data)
        if not registered:
            Label(screen1, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()

    def login_verify():
        global username1
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)
        username1 = username1 + ".cacc"
        tfk = open("Token.txt", "r")
        token_ = tfk.read()
        tfk.close()
        g = Github(token_)
        Account_Database = g.get_user().get_repo("AccountData")
        contents = Account_Database.get_contents("")
        for c in contents:
            user_info = username1
            if user_info == c.name:
                verify = str(c.decoded_content).replace("b", "")
                verify = verify.replace("'", "")
                if password1 in verify:
                    global username
                    username = username1
                    f = open("Logged.txt", "w")
                    f.write(username)
                    f.close()
                    screen.destroy()
                    os.system('ServerSelect.pyw')
                else:
                    password_not_recognised()

            else:
                user_not_found()

    def register():
        global screen1
        screen1 = Toplevel(screen)
        screen1.title("Register")
        screen1.geometry("300x250")
        screen1.iconbitmap('CC logo.ico')

        global username
        global password
        global username_entry
        global password_entry
        username = StringVar()
        password = StringVar()

        Label(screen1, text="Please enter details below").pack()
        Label(screen1, text="").pack()
        Label(screen1, text="Username * ").pack()

        username_entry = Entry(screen1, textvariable=username)
        username_entry.pack()
        Label(screen1, text="Password * ").pack()
        password_entry = Entry(screen1, textvariable=password)
        password_entry.pack()
        Label(screen1, text="").pack()
        Button(screen1, text="Register", width=10, height=1, command=register_user).pack()

    def login():
        global screen2
        screen2 = Toplevel(screen)
        screen2.title("Login")
        screen2.geometry("300x250")
        screen2.iconbitmap('CC logo.ico')
        Label(screen2, text="Please enter details below to login").pack()
        Label(screen2, text="").pack()

        global username_verify
        global password_verify

        username_verify = StringVar()
        password_verify = StringVar()

        global username_entry1
        global password_entry1

        Label(screen2, text="Username * ").pack()
        username_entry1 = Entry(screen2, textvariable=username_verify)
        username_entry1.pack()
        Label(screen2, text="").pack()
        Label(screen2, text="Password * ").pack()
        password_entry1 = Entry(screen2, textvariable=password_verify)
        password_entry1.pack()
        Label(screen2, text="").pack()
        Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()

    def main_screen():
        global screen
        screen = Tk()
        screen.geometry("300x250")
        screen.title("CC Login")
        screen.iconbitmap('CC logo.ico')
        Label(text="Login to CharonChat", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Login", height="2", width="30", command=login).pack()
        Label(text="").pack()
        Button(text="Register", height="2", width="30", command=register).pack()

        screen.mainloop()

    main_screen()


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
        self.join_button = None
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
        def hello():
            def run():
                os.chdir("files_current")
                os.startfile(filename)

            def download():
                try:
                    shutil.move(fr"files_current\{filename}", fr"C:\Users\{getpass.getuser()}\Desktop")
                    Label(root, text="The file is on your desktop", foreground="green").pack()
                except shutil.Error:
                    Label(root, text="The file is already on your desktop", foreground="red").pack()
            root = Tk()
            root.title(filename)
            root.geometry("250x300")
            Button(root, text="Run (Download and then run)", command=lambda: run(), state=DISABLED).pack()
            Button(root, text="Download", command=lambda: download()).pack()
            root.mainloop()
        while True:
            buffer = so.recv(256)
            if not buffer:
                break
            message = buffer.decode('utf-8')
            if "@logserverusage@" in message:
                pass
            elif "<f:" in message:
                hyperlink = HyperlinkManager(self.chat_transcript_area)
                filename = str(message).replace("<f:", "")
                print(message)
                try:
                    un, un2, filename = str(message).split(":")
                    print(filename)
                    wget.download(f"https://raw.githubusercontent.com/Charonum/PendFChat/main/{filename}",
                                fr"files_current\{filename}")
                    self.chat_transcript_area.insert(END, f'{un}: ')
                    self.chat_transcript_area.insert(END, filename, hyperlink.add(hello))
                    self.chat_transcript_area.insert(END, '\n')
                    self.chat_transcript_area.yview(END)
                except:
                    pass
            else:
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)

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
        self.enter_text_widget = Text(frame, width=65, height=3, font=("Serif", 12))
        self.enter_text_widget.pack(side='left', pady=15)
        self.enter_text_widget.bind('<Return>', self.on_enter_key_pressed)
        frame.pack(side='top', anchor=W)
        Button(self.root, text="Send File", command=lambda: self.send()).pack()

    def send(self):
        file = askopenfile(mode='rb')
        backslash_int = 0
        for backslash in file.name.split("/"):
            backslash_int = backslash_int + 1
        backslash_int = backslash_int - 1
        filename = file.name.split("/")[backslash_int]
        tfk = open("Token.txt", "r")
        token_ = tfk.read()
        tfk.close()
        g = Github(token_)
        Account_Database = g.get_user().get_repo("PendFChat")
        Account_Database.create_file(filename, "Added chat pending file", file.read())
        def hello():
            def run():
                os.chdir("files_current")
                os.startfile(filename)

            def download():
                try:
                    shutil.move(fr"files_current\{filename}", fr"C:\Users\{getpass.getuser()}\Desktop")
                    Label(root, text="The file is on your desktop", foreground="green").pack()
                except shutil.Error:
                    Label(root, text="The file is already on your desktop", foreground="red").pack()

            root = Tk()
            root.title(filename)
            root.geometry("250x300")
            Button(root, text="Run (Download and then run)", command=lambda: run(), state=DISABLED).pack()
            Button(root, text="Download", command=lambda: download()).pack()
            root.mainloop()
        hyperlink = HyperlinkManager(self.chat_transcript_area)
        print(filename)
        wget.download(f"https://raw.githubusercontent.com/Charonum/PendFChat/main/{filename}",
                        fr"files_current\{filename}")
        self.chat_transcript_area.insert(END, f'{self.username}: ')
        self.chat_transcript_area.insert(END, filename, hyperlink.add(hello))
        self.chat_transcript_area.insert(END, '\n')
        self.chat_transcript_area.yview(END)
        self.client_socket.send(f"{self.username}: <f:{filename}".encode("utf-8"))

    def on_join(self):
        self.client_socket.send((self.username + " has joined").encode('utf-8'))

    def on_enter_key_pressed(self, event):
        self.send_chat()
        self.clear_text()

    def clear_text(self):
        self.enter_text_widget.delete(1.0, 'end')

    def send_chat(self):
        senders_name = self.username + ": "
        data = self.enter_text_widget.get(1.0, 'end').strip()
        message = (senders_name + data).encode('utf-8')
        self.chat_transcript_area.insert('end', message.decode('utf-8') + '\n')
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
            for file in os.listdir("files_current"):
                os.remove(fr"files_current\{file}")
            os.system("ServerSelect.pyw")
            exit(0)


if __name__ == '__main__':
    login()
