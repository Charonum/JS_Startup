import os
import wget
import requests
import getpass

print("Removing Old Files...")

path = fr"C:\Users\{getpass.getuser()}\Charonum\JS"
for item in os.listdir(path):
    item = os.path.join(path, item)
    os.remove(item)

print("Done!")

response = requests.get('https://raw.githubusercontent.com/Charonum/JSCode/main/Files.txt')
responsecontent = response.text
for file in responsecontent.split("\n"):
    file = file.replace("b'", "")
    file = file.replace("'", "")
    file = file.replace(r"\n", "")
    if file == "":
        pass
    elif file == "setup.py":
        pass
    elif ".py" in file:
        url = f'https://raw.githubusercontent.com/Charonum/JSCode/main/code/windows/{file}'
        print(f"Fetching {url}")
        wget.download(url)
    elif ".pyw" in file:
        url = f'https://raw.githubusercontent.com/Charonum/JSCode/main/code/windows/{file}'
        print(f"Fetching {url}")
        wget.download(url)


print("Fixing Errors...")

os.remove("Version.txt")
os.rename("Version (1).txt", "Version.txt")

print("Done!")
print("Update Complete")

os.system("ServerSelect.pyw")

quit()
