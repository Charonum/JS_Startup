from github import Github
from tkinter import *
from tkinter.filedialog import askopenfile
import os
os.system("TASKKILL /F /IM cmd.exe")
user = open("Logged.txt", "r").read().replace(".cacc", "")


def save():
    if newname.get() == '':
        tfk = open("Token.txt", "r")
        token_ = tfk.read()
        tfk.close()
        g = Github(token_)
        Pfp_Database = g.get_user().get_repo("AccountPfps")
        u = Pfp_Database.get_contents(f"{user}.txt")
        Pfp_Database.update_file(path=u.path, content=bioe.get(), message="active", sha=u.sha)
    else:
        newuser = newname.get()
        try:
            tfk = open("Token.txt", "r")
            token_ = tfk.read()
            tfk.close()
            g = Github(token_)
            Pfp_Database = g.get_user().get_repo("AccountData")
            u = Pfp_Database.get_contents(f"{user}.cacc")
            password = u.content.split("\n")[1]
            Pfp_Database.create_file(f"{newuser}.cacc", f"{newuser}\n{password}", "active")
            Label(root5, text="User Already Exists!", fg="red").pack()
            newname.delete(0, END)
        except:
            tfk = open("Token.txt", "r")
            token_ = tfk.read()
            tfk.close()
            g = Github(token_)
            Pfp_Database = g.get_user().get_repo("AccountData")
            u = Pfp_Database.get_contents(f"{user}.cacc")
            password = u.content.split("\n")[1]
            con = newuser + "\n" + password
            Pfp_Database.update_file(path=u.path, content=con, message="active", sha=u.sha)
            Label(root5, text="Settings Saved Successfully!\nThis will take up to 2 minutes to update.",
                  fg="green").pack()
            newname.delete(0, END)


def open_file():
    def add():
        tfk = open("Token.txt", "r")
        token_ = tfk.read()
        tfk.close()
        g = Github(token_)
        Pfp_Database = g.get_user().get_repo("AccountPfps")
        try:
            u = Pfp_Database.get_contents(f"{user}.png")
            Pfp_Database.update_file(path=u.path, content=content, message="active", sha=u.sha)
        except:
            Pfp_Database.create_file(f"{user}.png", "active", content)
        Label(root5, text=f"Profile Picture Uploaded!\nThis will become public in 24 hours.",
              foreground="green").pack()

    file = askopenfile(mode='rb', filetypes=[('PNG Image Files', '*.png')])
    content = file.read()
    add()


root5 = Tk()
root5.title("Settings")
root5.iconbitmap("CC logo.ico")
root5.geometry("250x300")
Label(root5, text=f"Logged in as: {user}", font=("Arial", 12, "bold")).pack()
Label(root5, text="").pack(anchor="w")
Label(root5, text="Change Name:").pack(anchor="w")
newname = Entry(root5)
newname.pack(anchor="w")
errorw = Label(root5, text="Change Bio:")
errorw.pack(anchor="w")
bio = open(rf"user_data\{user}.txt").read()
bioe = Entry(root5, width=0)
bioe.pack(anchor="w")
bioe.insert(0, bio)
Button(root5, text="Change Profile Picture", command=lambda: open_file()).pack()
Label(root5, text="").pack(anchor="w")
Label(root5, text="").pack(anchor="w")
Button(root5, text="Save", command=save).pack()
root5.mainloop()