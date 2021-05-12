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
        self.log_socket.send((self.username + " has joined").encode('utf-8'))
        self.listen_for_incoming_messages_in_a_thread()

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
        logthread = threading.Thread(target=self.recive_log_data)
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
            engine.say(message)
            engine.runAndWait()

        so.close()

    def gui(self):
        def on_close_window():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                leave()

        def leave():
            import os
            root.destroy()
            self.log_socket.send((self.username + " has left").encode('utf-8'))
            os.system("TASKKILL /F /IM pythonw.exe")
            os.system("TASKKILL /F /IM pyw.exe")
            os.system("ServerSelect.pyw")

        root = Tk()
        root.geometry("200x200")
        root.protocol("WM_DELETE_WINDOW", on_close_window)
        root.title("VC")
        root.iconbitmap("phone.ico")
        Label(root, text='You are in VC', font=(
            'Verdana', 15)).pack(side=TOP, pady=10)
        photo = PhotoImage(file="phone.png")
        photoimage = photo.subsample(5, 5)
        Button(root, text='Leave Call', image=photoimage,
               compound=LEFT, command=leave).pack(side=TOP)
        root.mainloop()

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
