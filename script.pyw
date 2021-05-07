from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import os
os.system("TASKKILL /F /IM cmd.exe")

root = Tk()
root.geometry('235x200')
root.title("Script Creator")
root.iconbitmap("CC logo.ico")

def open_file():
    def add():
        danger_label.destroy()
        k_button.destroy()
        str(file.name).replace("\\", "/")
        script_file = open(f"{str(file.name)}.pyw", "w")
        script_file.write(content)
        script_file.close()
        Label(text=f"Data Loaded! The script is now ready to use.", foreground="green").pack()
    file = askopenfile(mode='r', filetypes=[('CC Script Files', '*.csa')])
    if file is not None:
        danger_label = Label(root,
                text="Running a .csa script could change\nthe way CharonChat runs. Please\nconfirm that you understand",
                foreground="red")
        danger_label.pack()
        k_button = Button(root, text="OK", command=lambda: add())
        k_button.pack()
        content = file.read()


btn = Button(root, text='Open', command=lambda: open_file())
btn.pack(side=TOP, pady=10)

mainloop()