import socket
import threading
import pyaudio
from tkinter import *
from tkinter import messagebox
import os
import pyttsx3

engine = pyttsx3.init()
os.system("TASKKILL /F /IM cmd.exe")


class Client:
    def __init__(self):
        f = open("Logged.txt", "r")
        self.username = f.read()
        self.username = self.username.replace(".cacc", "")
        f.close()
        self.log_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_ip = '50.113.72.248'
        remote_port = 55888
        self.log_socket.connect((remote_ip, remote_port))
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.log_socket.send(("@logserverusage@" + self.username + " has joined").encode('utf-8'))
        self.listen_for_incoming_messages_in_a_thread()
        self.ip_list = []
        self.client_list = []

        while 1:
            try:
                self.target_ip = "50.113.72.248"
                self.target_port = 50001

                self.s.connect((self.target_ip, self.target_port))

                break
            except:
                print("Couldn't connect to server")

        chunk_size = 1024  # 512
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 20000

        # initialise microphone recording
        self.p = pyaudio.PyAudio()
        self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True,
                                          frames_per_buffer=chunk_size)
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True,
                                            frames_per_buffer=chunk_size)

        # start threads
        receive_thread = threading.Thread(target=self.receive_server_data)
        receive_thread.start()
        guithread = threading.Thread(target=self.gui)
        guithread.start()
        client_thread = threading.Thread(target=self.client_check)
        client_thread.start()
        self.send_data_to_server()

    def listen_for_incoming_messages_in_a_thread(self):
        thread = threading.Thread(target=self.recive_log_data, args=(self.log_socket,))
        thread.start()

    def recive_log_data(self, so):
        while True:
            buffer = so.recv(256)
            if not buffer:
                break
            message = buffer.decode('utf-8')
            if "@logserverusage@" in message:
                message = str(message)
                if "cl:" in message:
                    lisst = message.replace("@logserverusage@cl:", "")
                    lisst = lisst.replace(",", "")
                    lisst = lisst.replace("[", "")
                    lisst = lisst.replace("]", "")
                    lisst = lisst.replace("'", "")
                    self.ip_list = lisst.split()
                else:
                    engine.say(message.replace("@logserverusage@", ""))
                    engine.runAndWait()

        so.close()

    def client_check(self):
        while True:
            if len(self.ip_list) == 11:
                self.temp_ip_list = str(self.ip_list)
                if "192.168.1.1" in self.temp_ip_list:
                    if "Charonum" in self.client_list:
                        pass
                    else:
                        self.client_list.append("Charonum")
                if "75.32.225.157" in self.temp_ip_list:
                    if "STAWWWY" in self.client_list:
                        pass
                    else:
                        self.client_list.append("STAWWWY")
                if "66.27.125.154" in self.temp_ip_list:
                    if "Sealy" in self.client_list:
                        pass
                    else:
                        self.client_list.append("Sealy")
            else:
                if 11 < len(self.ip_list):
                    people_online = len(self.ip_list) / 11
                    rand_int = 0
                    while True:
                        if rand_int < people_online:
                            rand_int = rand_int + 1
                            full_int = 11 * rand_int
                            g_int = 10 * rand_int
                            l_int = 9 * rand_int
                            s_int = 8 * rand_int
                            sl_int = 7 * rand_int
                            ssl_int = 6 * rand_int
                            sa_int = 5 * rand_int
                            fsl_int = 4 * rand_int
                            s = 3 * rand_int
                            a = 2 * rand_int
                            d = 1 * rand_int
                            self.ip_list.append((self.ip_list[d] + self.ip_list[a] + self.ip_list[s] + self.ip_list[
                                fsl_int] + self.ip_list[sa_int] + self.ip_list[ssl_int] + self.ip_list[sl_int] +
                                                 self.ip_list[s_int] + self.ip_list[l_int] + self.ip_list[g_int] +
                                                 self.ip_list[full_int]))
                        else:
                            return
                        return
                    return
                else:
                    self.temp_ip_list = str(self.ip_list)
                    if "192.168.1.1" in self.temp_ip_list:
                        if "Charonum" in self.client_list:
                            pass
                        else:
                            self.client_list.append("Charonum")
                    if "75.32.225.157" in self.temp_ip_list:
                        if "STAWWWY" in self.client_list:
                            pass
                        else:
                            self.client_list.append("STAWWWY")
                    if "66.27.125.154" in self.temp_ip_list:
                        if "Sealy" in self.client_list:
                            pass
                        else:
                            self.client_list.append("Sealy")

    def gui(self):
        def open_online():
            root = Tk()
            root.geometry("100x100")
            Label(root, text=self.client_list).pack()
            root.mainloop()

        def on_close_window():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                leave()

        def leave():
            import os
            self.root.destroy()
            self.log_socket.send(("@logserverusage@" + self.username + " has left").encode('utf-8'))
            os.system("TASKKILL /F /IM pythonw.exe")
            os.system("TASKKILL /F /IM pyw.exe")
            os.system("ServerSelect.pyw")

        self.root = Tk()
        self.root.geometry("200x200")
        self.root.protocol("WM_DELETE_WINDOW", on_close_window)
        self.root.title("VC")
        self.root.iconbitmap("phone.ico")
        Label(self.root, text='You are in VC', font=(
            'Verdana', 15)).pack(side=TOP, pady=10)
        photo = PhotoImage(file="phone.png")
        photoimage = photo.subsample(5, 5)
        Button(self.root, text='Leave Call', image=photoimage,
               compound=LEFT, command=leave).pack(side=TOP)
        Button(self.root, text="Online People in This Chat", command=lambda: open_online()).pack()
        self.root.mainloop()

    def receive_server_data(self):
        while True:
            try:
                data = self.s.recv(1024)
                self.playing_stream.write(data)
            except:
                pass

    def send_data_to_server(self):
        while True:
            try:
                data = self.recording_stream.read(1024)
                self.s.sendall(data)
            except:
                pass


client = Client()
