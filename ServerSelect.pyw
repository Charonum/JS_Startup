from tkinter import *
import os
import socket

os.system("TASKKILL /F /IM cmd.exe")
online_list = None
offline_list = None


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
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote_ip = '50.113.72.248'
                remote_port = 55888
                client_socket.connect((remote_ip, remote_port))
                online_list.append("vcl")
            except:
                offline_list.append("vcl")
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
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote_ip = '50.113.72.248'
                remote_port = 55888
                client_socket.connect((remote_ip, remote_port))
                online_list.append("vcl")
            except:
                offline_list.append("vcl")
        except:
            offline_list.append("vcm")
            try:
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote_ip = '50.113.72.248'
                remote_port = 55888
                client_socket.connect((remote_ip, remote_port))
                online_list.append("vcl")
            except:
                offline_list.append("vcl")


refresh()
print(f"Online: {online_list}")
print(f"Offline: {offline_list}")


def runmain():
    screen.destroy()
    os.system("JSMain.pyw")
    quit()


def logout():
    s = open("Logged.txt", "r+")
    s.seek(0)
    s.truncate(0)
    s.close()
    quit()


def guireport():
    global error_
    root = Tk()
    root.title("CharonChat")
    root.iconbitmap("CC logo.ico")
    root.geometry("250x300")
    Label(root, text="What is the bug?").pack()
    error_ = Entry(root, width=20)
    error_.pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Label(root, text="").pack()
    Button(root, text="Report", command=report).pack()
    root.mainloop()


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


def voc():
    screen.destroy()
    os.system("vc.pyw")
    quit()


def settingsf():
    def save():
        newuser = newname.get()
        try:
            f2 = open(str(newuser), "r")
            f2.close()
            Label(root, text="User Already Exists!", fg="red").pack()
            newname.delete(0, END)
        except:
            import os
            os.rename(str(user), str(newuser))
            f6 = open("Logged.txt", "w")
            f6.write(str(newuser))
            f6.close()
            Label(root, text="Settings Saved Successfully! Restart\nthe program for this to take action",
                  fg="green").pack()
            newname.delete(0, END)

    root = Tk()
    root.title("Settings")
    root.iconbitmap("CC logo.ico")
    root.geometry("250x300")
    Label(root, text=f"Logged in as: {user}", font=("Arial", 12, "bold")).pack()
    Label(root, text="").pack(anchor="w")
    Label(root, text="Change Name:").pack(anchor="w")
    newname = Entry(root, width=20)
    newname.pack(anchor="w")
    errorw = Label(root, text="")
    errorw.pack(anchor="w")
    Label(root, text="").pack(anchor="w")
    Label(root, text="").pack(anchor="w")
    Label(root, text="").pack(anchor="w")
    Label(root, text="").pack(anchor="w")
    Button(root, text="Save", command=save).pack()
    root.mainloop()


def alex():
    import os
    screen.destroy()
    os.system("alex.pyw")
    quit()


def char():
    import os
    screen.destroy()
    os.system("charump.pyw")
    quit()


def status():
    root = Tk()
    root.title("CharonChat")
    root.iconbitmap("CC logo.ico")
    root.geometry("250x300")

    def refresh1(offline_number=0):
        if "tcm" in online_list:
            if "vcm" in online_list:
                if "vcl" in online_list:
                    statu = Label(root, text="All servers status: Online", fg="green",
                                  font=("Arial", 12, "bold")).pack()
                else:
                    offline_number = offline_number + 1
                    statu = Label(root, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                  font=("Arial", 12, "bold")).pack()
            else:
                offline_number = offline_number + 1
                if "vcl" in online_list:
                    if offline_number == 0:
                        statu = Label(root, text="All servers status: Online", fg="green",
                                      font=("Arial", 12, "bold")).pack()
                    else:
                        statu = Label(root, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                      font=("Arial", 12, "bold")).pack()
                else:
                    offline_number = offline_number + 1
                    statu = Label(root, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                  font=("Arial", 12, "bold")).pack()
        else:
            offline_number = offline_number + 1
            if "vcm" in online_list:
                if "vcl" in online_list:
                    if offline_number == 0:
                        statu = Label(root, text="All servers status: Online", fg="green",
                                      font=("Arial", 12, "bold")).pack()
                    else:
                        statu = Label(root, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                      font=("Arial", 12, "bold")).pack()
                else:
                    offline_number = offline_number + 1
                    statu = Label(root, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                  font=("Arial", 12, "bold")).pack()
            else:
                offline_number = offline_number + 1
                if "vcl" in online_list:
                    if offline_number == 0:
                        statu = Label(root, text="All servers status: Online", fg="green",
                                      font=("Arial", 12, "bold")).pack()
                    else:
                        statu = Label(root, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                      font=("Arial", 12, "bold")).pack()
                else:
                    offline_number = offline_number + 1
                    statu = Label(root, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                  font=("Arial", 12, "bold")).pack()

        if "tcm" in online_list:
            tcm = Label(root, text="'tcm', identified as Text Chat status: Online", fg="green").pack()
        elif "tcm" in offline_list:
            tcm = Label(root, text="'tcm', identified as Text Chat status: Offline", fg="red").pack()
        else:
            tcm = Label(root, text="'tcm', identified as Text Chat status: Unknown", fg="red").pack()
        if "vcm" in online_list:
            vcm = Label(root, text="'vcm', identified as Main VC status: Online", fg="green").pack()
        elif "vcm" in offline_list:
            vcm = Label(root, text="'vcm', identified as Main VC status: Offline", fg="red").pack()
        else:
            vcm = Label(root, text="'vcm', identified as Main VC status: Unknown", fg="red").pack()
        if "vcl" in online_list:
            vcl = Label(root, text="'tcm', identified as VC Log status: Online", fg="green").pack()
        elif "vcl" in offline_list:
            vcl = Label(root, text="'tcm', identified as VC Log status: Offline", fg="red").pack()
        else:
            vcl = Label(root, text="'tcm', identified as VC Log status: Unknown", fg="red").pack()

    def refresh2(offline_number=0):
        refresh()
        root2 = Tk()
        root2.title("CharonChat")
        root2.iconbitmap("CC logo.ico")
        root2.geometry("250x300")
        if "tcm" in online_list:
            if "vcm" in online_list:
                if "vcl" in online_list:
                    statu = Label(root2, text="All servers status: Online", fg="green",
                                  font=("Arial", 12, "bold")).pack()
                else:
                    offline_number = offline_number + 1
                    statu = Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                  font=("Arial", 12, "bold")).pack()
            else:
                offline_number = offline_number + 1
                if "vcl" in online_list:
                    if offline_number == 0:
                        statu = Label(root2, text="All servers status: Online", fg="green",
                                      font=("Arial", 12, "bold")).pack()
                    else:
                        statu = Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                      font=("Arial", 12, "bold")).pack()
                else:
                    offline_number = offline_number + 1
                    statu = Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                  font=("Arial", 12, "bold")).pack()
        else:
            offline_number = offline_number + 1
            if "vcm" in online_list:
                if "vcl" in online_list:
                    if offline_number == 0:
                        statu = Label(root2, text="All servers status: Online", fg="green",
                                      font=("Arial", 12, "bold")).pack()
                    else:
                        statu = Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                      font=("Arial", 12, "bold")).pack()
                else:
                    offline_number = offline_number + 1
                    statu = Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                  font=("Arial", 12, "bold")).pack()
            else:
                offline_number = offline_number + 1
                if "vcl" in online_list:
                    if offline_number == 0:
                        statu = Label(root2, text="All servers status: Online", fg="green",
                                      font=("Arial", 12, "bold")).pack()
                    else:
                        statu = Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                      font=("Arial", 12, "bold")).pack()
                else:
                    offline_number = offline_number + 1
                    statu = Label(root2, text=f"All servers status: {str(offline_number)} offline", fg="red",
                                  font=("Arial", 12, "bold")).pack()

        if "tcm" in online_list:
            tcm = Label(root2, text="'tcm', identified as Text Chat status: Online", fg="green").pack()
        elif "tcm" in offline_list:
            tcm = Label(root2, text="'tcm', identified as Text Chat status: Offline", fg="red").pack()
        else:
            tcm = Label(root2, text="'tcm', identified as Text Chat status: Unknown", fg="red").pack()
        if "vcm" in online_list:
            vcm = Label(root2, text="'vcm', identified as Main VC status: Online", fg="green").pack()
        elif "vcm" in offline_list:
            vcm = Label(root2, text="'vcm', identified as Main VC status: Offline", fg="red").pack()
        else:
            vcm = Label(root2, text="'vcm', identified as Main VC status: Unknown", fg="red").pack()
        if "vcl" in online_list:
            vcl = Label(root2, text="'tcm', identified as VC Log status: Online", fg="green").pack()
        elif "vcl" in offline_list:
            vcl = Label(root2, text="'tcm', identified as VC Log status: Offline", fg="red").pack()
        else:
            vcl = Label(root2, text="'tcm', identified as VC Log status: Unknown", fg="red").pack()
        root2.mainloop()

    refresh1()
    Button(root, text="Refresh", command=refresh2).pack()
    root.mainloop()


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


screen = Tk()
screen.geometry("610x390")
screen.title("CharonChat")
screen.iconbitmap('CC logo.ico')
f = open("Logged.txt", "r")
user = f.read()
f.close()
user = user.replace(".cacc", "")
Label(text=f"Welcome, {user}", bg="grey", width="500", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()
if "tcm" in online_list:
    universal = Button(screen, text="Join Text Chat", height=1, command=runmain).pack()
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
    if "vcl" in online_list:
        vc = Button(screen, text="Join VC", height=1, command=voc).pack()
    else:
        import smtplib

        sender_address = "jonahprogrambot@gmail.com"
        receiver_address = "jonahjwalsh@gmail.com"
        account_password = "skro7576"
        subject = "VC log offline"
        body = f"VC server log is offline!\nAutomated message from {user}"
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
            smtp_server.login(sender_address, account_password)
            message = f"Subject: {subject}\n\n{body}"
            smtp_server.sendmail(sender_address, receiver_address, message)
        vc = Button(screen, text="Join VC: Offline!", height=1, state=DISABLED).pack()
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
    vc = Button(screen, text="Join VC: Offline!", height=1, state=DISABLED).pack()
chat = Button(screen, text="Report A Bug", height=1, command=guireport).pack()
settings = Button(screen, text="Settings", height=1, command=settingsf).pack()
alex = Button(screen, text="Chat With A.L.E.X.", height=1, command=alex).pack()
charump = Button(screen, text="Chat With Charump", height=1, command=char).pack()
script2 = Button(screen, text="Scripts", height=1, command=lambda: script()).pack()
online_servers = Button(screen, text="Servers Status", height=1, command=status).pack()
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
chat_transcript_area.insert('end', "now you can see if chats are offline yes very cool\nv1.1.7")
chat_transcript_area.yview(END)
screen.mainloop()
