from tkinter import *
import os

os.system("TASKKILL /F /IM cmd.exe")


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
    global error
    root = Tk()
    root.title("CharonChat")
    root.iconbitmap("CC logo.ico")
    root.geometry("250x300")
    Label(root, text="What is the bug?").pack()
    error = Entry(root, width=20)
    error.pack()
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
    sender_address = "jonahprogrambot@gmail.com"  # Replace this with your Gmail address
    receiver_address = "jonahjwalsh@gmail.com"  # Replace this with any valid email address
    account_password = "skro7576"  # Replace this with your Gmail account password
    subject = "Bug Report"
    body = f"{user} reported a bug\n{error.get()}"
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_server:
        smtp_server.login(sender_address, account_password)
        message = f"Subject: {subject}\n\n{body}"
        smtp_server.sendmail(sender_address, receiver_address, message)


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


def script():
    import os
    def new_script():
        os.system("script.pyw")

    def script_settings(script, required_script):
        def run_script():
            screen.destroy()
            root2.destroy()
            roof.destroy()
            os.system(required_script)
            quit()
        def remove():
            os.remove(required_script)
            Label(root2, text=f"{script} was removed.", foreground="green")
        root2 = Tk()
        root2.title(script)
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
screen.geometry("595x370")
screen.title("CharonChat")
screen.iconbitmap('CC logo.ico')
f = open("Logged.txt", "r")
user = f.read()
f.close()
user = user.replace(".cacc", "")
Label(text=f"Welcome, {user}", bg="grey", width="500", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()
universal = Button(screen, text="Join Universal Chat", height=1, command=runmain).pack()
vc = Button(screen, text="Join VC", height=1, command=voc).pack()
chat = Button(screen, text="Report A Bug", height=1, command=guireport).pack()
settings = Button(screen, text="Settings", height=1, command=settingsf).pack()
alex = Button(screen, text="Chat With A.L.E.X.", height=1, command=alex).pack()
charump = Button(screen, text="Chat With Charump", height=1, command=char).pack()
script2 = Button(screen, text="Scripts", height=1, command=lambda: script()).pack()
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
chat_transcript_area.insert('end', "script imports here cool\nv1.1.5")
chat_transcript_area.yview(END)
screen.mainloop()
