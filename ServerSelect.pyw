import datetime
import os
import socket
from tkinter import *

import requests
import wget
from PIL import ImageTk, Image
from github import Github

f = open("Logged.txt", "r")
user = f.read()
f.close()

ip = requests.get('http://ip.42.pl/raw').text

os.system("TASKKILL /F /IM cmd.exe")
user_list = []


def group():
    os.system("group.pyw")
    screen.destroy()
    quit()


def new_close():
    quit()


def uninstall():
    for file in os.listdir():
        os.remove(file)


online_list = None
offline_list = None
if ip == "75.32.225.157":
    pass
elif ip == "66.27.125.154":
    pass
elif ip == "50.113.72.248":
    pass
elif ip == "104.172.4.74":
    pass
else:
    root = Tk()
    root.title("Unsupported IP")
    root.geometry("250x300")
    root.iconbitmap("CC logo.ico")
    Label(root, text=f"You have an unsupported IP. Your IP: {ip}\nYou can uninstall the program here:\n|\n|\nv").pack()
    Button(root, text="Uninstall", command=uninstall).pack()
    root.protocol("WM_DELETE_WINDOW", lambda: new_close())
    root.mainloop()

tfk = open("Token.txt", "r")
token_ = tfk.read()
tfk.close()
g = Github(token_)
Account_Database = g.get_user().get_repo("AccountData")
contents = Account_Database.get_contents("")
for content in contents:
    user_ = content.name
    user_ = user_.replace(".cacc", "")
    user_list.append(user_)
Pfp_Database = g.get_user().get_repo("AccountPfps")
s = Pfp_Database.get_contents("")
for f in os.listdir("user_data"):
    if "rel" in f:
        pass
    else:
        os.remove(rf"user_data\{f}")
for file in s:
    file = file.name
    file = file.replace("b'", "")
    file = file.replace("'", "")
    file = file.replace(r"\n", "")
    if file == "":
        pass
    else:
        url = f'https://raw.githubusercontent.com/Charonum/AccountPfps/main/{file}'
        wget.download(url, "user_data")


def refresh():
    global offline_list
    global online_list
    online_list = []
    offline_list = []
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        remote_ip = '50.113.72.248'
        remote_port = 25565
        client_socket.connect((remote_ip, remote_port))
        online_list.append("tcm")
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = '50.113.72.248'
            remote_port = 50001
            client_socket.connect((remote_ip, remote_port))
            online_list.append("vcm")
        except:
            offline_list.append("vcm")
    except:
        offline_list.append("tcm")
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_ip = '50.113.72.248'
            remote_port = 50001
            client_socket.connect((remote_ip, remote_port))
            online_list.append("vcm")
        except:
            offline_list.append("vcm")


refresh()


def runmain():
    def main():
        screen.destroy()
        os.system("JSMain.pyw")
        quit()

    root = Tk()
    root.title("Text Chat")
    root.geometry("250x300")
    root.iconbitmap("CC logo.ico")
    Button(root, text="Main Chat", command=lambda: main()).pack()
    Button(root, text="Group Chat", command=lambda: group()).pack()
    root.mainloop()


def logout():
    s = open("Logged.txt", "r+")
    s.seek(0)
    s.truncate(0)
    s.close()
    quit()


def guireport():
    global error_
    root6 = Tk()
    root6.title("CharonChat")
    root6.iconbitmap("CC logo.ico")
    root6.geometry("250x300")
    Label(root6, text="What is the bug?").pack()
    error_ = Entry(root6, width=20)
    error_.pack()
    Label(root6, text="").pack()
    Label(root6, text="").pack()
    Label(root6, text="").pack()
    Label(root6, text="").pack()
    Label(root6, text="").pack()
    Label(root6, text="").pack()
    Label(root6, text="").pack()
    Button(root6, text="Report", command=report).pack()
    root6.mainloop()


def report():
    import smtplib
    sender_address_ = "jonahprogrambot@gmail.com"
    receiver_address_ = "jonahjwalsh@gmail.com"
    account_password_ = "skro7576"
    subject_ = "Bug Report"
    body_ = f"{user} reported a bug\n{error_.get()}"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server_:
        smtp_server_.login(sender_address_, account_password_)
        messages = f"Subject: {subject_}\n\n{body_}"
        smtp_server_.sendmail(sender_address_, receiver_address_, messages)


def dm():
    ff = open("dmuser.txt", "w")
    ff.write(str(user__))
    ff.close()
    os.system("dm.pyw")
    quit()


def search_user():
    root = Tk()

    def open_user(user__):
        global counted
        for file in os.listdir("user_data"):
            if user__ in file:
                counted = 0
                root6 = Tk()
                root6.title("CharonChat")
                root6.iconbitmap("CC logo.ico")
                root6.geometry("250x300")
                Label(root6, text=user__, font=("Arial", 12, "bold")).pack()
                Label(root6, text="Bio:", font=("Arial", 12, "bold")).pack()
                try:
                    bio = open(rf"user_data\{user__}.txt").read()
                except FileNotFoundError:
                    bio = f"{user__} has no bio."
                Label(root6, text=bio).pack()
                Label(root6, text="Profile Picture:", font=("Arial", 12, "bold")).pack()
                try:
                    pfp = Image.open(f"user_data/{user__}.png")
                    canvas = Canvas(root6, width=600, height=400)
                    canvas.pack()

                    # Resize the Image using resize method
                    resized_image = pfp.resize((70, 70), Image.ANTIALIAS)
                    new_image = ImageTk.PhotoImage(master=canvas, image=resized_image)

                    # Add image to the Canvas Items
                    canvas.create_image(125, 50, image=new_image)
                    Button(root6, text="DM", command=dm).pack()
                    root6.mainloop()
                except FileNotFoundError:
                    print("Hello")
                    Label(root6, text=f"{user__} has no profile picture").pack()
            else:
                counted = 1
        if counted >> 0:
            root6 = Tk()
            root6.title("CharonChat")
            root6.iconbitmap("CC logo.ico")
            root6.geometry("250x300")
            Label(root6, text=f"{user__} does not exist!", font=("Arial", 12, "bold")).pack()
            root6.mainloop()
        else:
            pass

    def update(data):
        list_.delete(0, END)
        for item in data:
            list_.insert(END, item)

    def r_fillout(e):
        user_ = entry.get()
        open_user(user_)

    def fillout(e):
        if list_.get(ANCHOR) == "No Users Found":
            pass
        else:
            entry.delete(0, END)
            entry.insert(0, list_.get(ANCHOR))
            user_ = entry.get()
            open_user(user_)

    def check(e):
        typed = entry.get()
        if typed == '':
            data = users
        else:
            data = []
            for item in users:
                if typed.lower() in item.lower():
                    data.append(item)
            if not data:
                data.append("No Users Found")
            else:
                try:
                    data.remove("No Users Found")
                except:
                    pass
        update(data)

    root.title("CharonChat")
    root.iconbitmap("CC logo.ico")
    root.geometry("500x300")
    Label(root, text="Start Typing...", font=("Helvetica", 14), foreground="grey").pack(pady=20)
    entry = Entry(root, font=("Helvetica", 20))
    entry.pack()
    list_ = Listbox(root, width=50)
    list_.pack(pady=40)
    users = user_list
    update(users)
    list_.bind("<<ListboxSelect>>", fillout)
    entry.bind("<Return>", r_fillout)
    entry.bind("<KeyRelease>", check)
    root.mainloop()


def user_dm():
    root = Tk()

    def open_user(user__):
        global counted
        for file in os.listdir("user_data"):
            if user__ in file:
                counted = 0
                root6 = Tk()
                root6.title("CharonChat")
                root6.iconbitmap("CC logo.ico")
                root6.geometry("250x300")
                rn = datetime.datetime.now().strftime('%d/%m/%Y').replace('/', '!')
                Label(root6, text=user__, font=("Arial", 12, "bold")).pack()
                Button(root6, text="DM", command=dm).pack()
                root6.mainloop()
            else:
                counted = 1
        if counted >> 0:
            root6 = Tk()
            root6.title("CharonChat")
            root6.iconbitmap("CC logo.ico")
            root6.geometry("250x300")
            Label(root6, text=f"{user__} does not exist!", font=("Arial", 12, "bold")).pack()
            root6.mainloop()
        else:
            pass

    def update(data):
        list_.delete(0, END)
        for item in data:
            list_.insert(END, item)

    def r_fillout(e):
        user_ = entry.get()
        open_user(user_)

    def fillout(e):
        if list_.get(ANCHOR) == "No Users Found":
            pass
        else:
            entry.delete(0, END)
            entry.insert(0, list_.get(ANCHOR))
            user_ = entry.get()
            open_user(user_)

    def check(e):
        typed = entry.get()
        if typed == '':
            data = users
        else:
            data = []
            for item in users:
                if typed.lower() in item.lower():
                    data.append(item)
            if not data:
                data.append("No Users Found")
            else:
                try:
                    data.remove("No Users Found")
                except:
                    pass
        update(data)

    root.title("CharonChat")
    root.iconbitmap("CC logo.ico")
    root.geometry("500x300")
    Label(root, text="Start Typing...", font=("Helvetica", 14), foreground="grey").pack(pady=20)
    entry = Entry(root, font=("Helvetica", 20))
    entry.pack()
    list_ = Listbox(root, width=50)
    list_.pack(pady=40)
    users = user_list
    update(users)
    list_.bind("<<ListboxSelect>>", fillout)
    entry.bind("<Return>", r_fillout)
    entry.bind("<KeyRelease>", check)
    root.mainloop()


def voc():
    screen.destroy()
    os.system("vc.pyw")
    quit()


def settingsf():
    root = Tk()
    root.title("Settings")
    root.geometry("250x300")
    root.iconbitmap("CC logo.ico")

    def sett():
        os.system("sett.py")

    Button(root, text="Account Settings", command=sett).pack()
    Button(root, text="Binary Settings (Dangerous)", command=binary).pack()


def ais():
    def alex():
        import os
        screen.destroy()
        root.destroy()
        os.system("alex.pyw")
        quit()

    def char():
        import os
        screen.destroy()
        root.destroy()
        os.system("charump.pyw")
        quit()

    root = Tk()
    root.title("A.I.s")
    root.geometry("250x300")
    root.iconbitmap("CC logo.ico")
    Button(root, text="Chat With A.L.E.X.", height=1, command=alex).pack()
    Button(root, text="Chat With Charump", height=1, command=char).pack()
    root.mainloop()


def status():
    root3 = Tk()
    root3.title("CharonChat")
    root3.iconbitmap("CC logo.ico")
    root3.geometry("250x300")

    def refresh1(offline_number=0):
        if "tcm" in online_list:
            if "vcm" in online_list:
                Label(root3, text="All servers status: Online", fg="green",
                      font=("Arial", 12, "bold")).pack()
            else:
                if offline_number == 0:
                    Label(root3, text="All servers status: Online", fg="green",
                          font=("Arial", 12, "bold")).pack()
                else:
                    Label(root3, text=f"All servers status: {str(offline_number)} offline", fg="red",
                          font=("Arial", 12, "bold")).pack()
        else:
            offline_number = offline_number + 1
            if "vcm" in online_list:
                if offline_number == 0:
                    Label(root3, text="All servers status: Online", fg="green",
                          font=("Arial", 12, "bold")).pack()
                else:
                    Label(root3, text=f"All servers status: {str(offline_number)} offline", fg="red",
                          font=("Arial", 12, "bold")).pack()
            else:
                offline_number = offline_number + 1
                if offline_number == 0:
                    Label(root3, text="All servers status: Online", fg="green",
                          font=("Arial", 12, "bold")).pack()
                else:
                    Label(root3, text=f"All servers status: {str(offline_number)} offline", fg="red",
                          font=("Arial", 12, "bold")).pack()

        if "tcm" in online_list:
            Label(root3, text="'tcm', identified as TC status: Online", fg="green").pack()
        elif "tcm" in offline_list:
            Label(root3, text="'tcm', identified as TC status: Offline", fg="red").pack()
        else:
            Label(root3, text="'tcm', identified as TC status: Unknown", fg="red").pack()
        if "vcm" in online_list:
            Label(root3, text="'vcm', identified as VC status: Online", fg="green").pack()
        elif "vcm" in offline_list:
            Label(root3, text="'vcm', identified as VC status: Offline", fg="red").pack()
        else:
            Label(root3, text="'vcm', identified as VC status: Unknown", fg="red").pack()

    def refresh2(offline_number=0):
        refresh()
        root2 = Tk()
        root2.title("CharonChat")
        root2.iconbitmap("CC logo.ico")
        root2.geometry("250x300")
        if "tcm" in online_list:
            if "vcm" in online_list:
                Label(root2, text="All servers status: Online", fg="green",
                      font=("Arial", 12, "bold")).pack()
            else:
                if offline_number == 0:
                    Label(root2, text="All servers status: Online", fg="green",
                          font=("Arial", 12, "bold")).pack()
                else:
                    Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                          font=("Arial", 12, "bold")).pack()
        else:
            offline_number = offline_number + 1
            if "vcm" in online_list:
                if offline_number == 0:
                    Label(root2, text="All servers status: Online", fg="green",
                          font=("Arial", 12, "bold")).pack()
                else:
                    Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                          font=("Arial", 12, "bold")).pack()
            else:
                offline_number = offline_number + 1
                if offline_number == 0:
                    Label(root2, text="All servers status: Online", fg="green",
                          font=("Arial", 12, "bold")).pack()
                else:
                    Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                          font=("Arial", 12, "bold")).pack()

        if "tcm" in online_list:
            Label(root2, text="'tcm', identified as TC status: Online", fg="green").pack()
        elif "tcm" in offline_list:
            Label(root2, text="'tcm', identified as TC status: Offline", fg="red").pack()
        else:
            Label(root2, text="'tcm', identified as TC status: Unknown", fg="red").pack()
        if "vcm" in online_list:
            Label(root2, text="'vcm', identified as VC status: Online", fg="green").pack()
        elif "vcm" in offline_list:
            Label(root2, text="'vcm', identified as VC status: Offline", fg="red").pack()
        else:
            Label(root2, text="'vcm', identified as VC status: Unknown", fg="red").pack()
        root2.mainloop()

    refresh1()
    Button(root3, text="Refresh", command=refresh2).pack()
    root3.mainloop()


def script():
    import os

    def new_script():
        os.system("script.pyw")

    def script_settings(script_, required_script):
        def run_script():
            screen.destroy()
            root2.destroy()
            roof.destroy()
            os.system(required_script)
            quit()

        def remove():
            os.remove(required_script)
            Label(root2, text=f"{script_} was removed.", foreground="green").pack()

        root2 = Tk()
        root2.title(script_)
        root2.iconbitmap("CC logo.ico")
        root2.geometry("250x300")
        Button(root2, text="Run", command=lambda: run_script()).pack()
        Button(root2, text="Uninstall", command=lambda: remove()).pack()
        root2.mainloop()

    roof = Tk()
    roof.title("Scripts")
    roof.iconbitmap("CC logo.ico")
    roof.geometry("250x300")
    for file in os.listdir():
        if ".csa" in file:
            if ".pyw" in file:
                file2 = file
                file3 = file
                file2 = file2.replace(".pyw", "")
                file2 = file2.replace(".csa", "")
                Button(roof, text=file2, command=lambda: script_settings(file2, file3)).pack()
    Button(roof, text="New Script", command=lambda: new_script()).pack()
    roof.mainloop()


def user__():
    root = Tk()
    root.title("Users")
    root.iconbitmap("CC logo.ico")
    root.geometry("250x300")
    Button(root, text="Search For Users", height=1, command=lambda: search_user()).pack()
    Button(root, text="DM Users", height=1, command=lambda: user_dm()).pack()
    root.mainloop()


screen = Tk()
screen.geometry("610x420")
screen.title("CharonChat")
screen.iconbitmap('CC logo.ico')
user = user.replace(".cacc", "")
Label(text=f"Welcome, {user}", bg="grey", width="500", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()
if "tcm" in online_list:
    universal = Button(screen, text="Text Chat", height=1, command=runmain).pack()
else:
    import smtplib

    sender_address = "jonahprogrambot@gmail.com"
    receiver_address = "jonahjwalsh@gmail.com"
    account_password = "skro7576"
    subject = "Text Chat is offline!"
    body = f"Text chat is offline!\nAutomated message from {user}"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender_address, account_password)
        message = f"Subject: {subject}\n\n{body}"
        smtp_server.sendmail(sender_address, receiver_address, message)
    universal = Button(screen, text="Join Text Chat: Offline!", height=1, state=DISABLED).pack()
if "vcm" in online_list:
    vc = Button(screen, text="Join VC", height=1, command=voc).pack()
else:
    import smtplib

    sender_address = "jonahprogrambot@gmail.com"
    receiver_address = "jonahjwalsh@gmail.com"
    account_password = "skro7576"
    subject = "Bug Report"
    body = f"VC server main is offline!\nAutomated message from {user}"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender_address, account_password)
        message = f"Subject: {subject}\n\n{body}"
        smtp_server.sendmail(sender_address, receiver_address, message)
    vc = Button(screen, text="VC: Offline!", height=1, state=DISABLED).pack()
chat = Button(screen, text="Report A Bug", height=1, command=guireport).pack()
settings = Button(screen, text="Settings", height=1, command=settingsf).pack()
Button(screen, text="A.I.s", height=1, command=ais).pack()
Button(screen, text="Users", height=1, command=lambda: user__()).pack()
script2 = Button(screen, text="Scripts", height=1, command=lambda: script()).pack()
online_servers = Button(screen, text="Servers Status", height=1, command=status).pack()


def binary():
    def load(script_):
        script_ = script_.get()
        data = f"https://raw.githubusercontent.com/Charonum/JS_Startup/main/{script_}"
        print(f"Script: {script_}\nURL: {data}")
        os.remove(script_)
        wget.download(data)
        Label(roof, text="Binary Refreshed", foreground="green").pack()

    roof = Tk()
    roof.title("Binary Refresh")
    roof.iconbitmap("CC logo.ico")
    roof.geometry("250x300")
    Label(roof, text=f"Only fill this out if you know\nwhat you are doing", fg="red",
          font=("Arial", 12, "bold")).pack()
    Label(roof, text="").pack()
    Label(roof, text="Script Name:").pack(anchor=W)
    pyscript = Entry(roof, width=15)
    pyscript.pack(anchor=W)
    Label(roof, text="").pack()
    Label(roof, text="").pack()
    Label(roof, text="").pack()
    Button(roof, text="Load", command=lambda: load(pyscript)).pack()
    roof.mainloop()


logout = Button(screen, text="Log Out", height=1, command=logout).pack()
frame = Frame()
Label(frame, text='Patch Notes:', font=("Serif", 12)).pack(side='top', anchor='w')
chat_transcript_area = Text(frame, width=60, height=3, font=("Serif", 12))
scrollbar = Scrollbar(frame, command=chat_transcript_area.yview, orient=VERTICAL)
chat_transcript_area.config(yscrollcommand=scrollbar.set)
chat_transcript_area.bind('<KeyPress>', lambda e: 'break')
chat_transcript_area.pack(side='left', padx=10)
scrollbar.pack(side='right', fill='y')
frame.pack(side='top')
chat_transcript_area.insert('end',
                            "bug fixes, organisation, DMs, group chat, and file sharing\nv1.2.4")
chat_transcript_area.yview(END)
screen.mainloop()
