import socket
import threading
import pyaudio
from tkinter import *
import os
os.system("TASKKILL /F /IM cmd.exe")

class Client:
    def __init__(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
        receive_thread = threading.Thread(target=self.receive_server_data).start()
        guithread = threading.Thread(target=self.gui).start()
        self.send_data_to_server()

    def gui(self):
        def leave():
            import os
            root.destroy()
            os.system("TASKKILL /F /IM pythonw.exe")
            os.system("TASKKILL /F /IM pyw.exe")
            os.system("ServerSelect.pyw")
        root = Tk()
        root.geometry("200x200")
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
