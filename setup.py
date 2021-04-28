import os
import wget
import requests
import getpass

print("Removing Old Files...")

path = fr"C:\Users\{getpass.getuser()}\Charonum\JS"
for item in os.listdir(path):
    if ".ico" in item:
        pass
    elif ".cacc" in item:
        pass
    elif "setup.py" == item:
        pass
    elif "Logged.txt" == item:
        pass
    else:
        item = os.path.join(path, item)
        os.remove(item)

print("Done!")

response = requests.get('https://raw.githubusercontent.com/Charonum/JSCode/main/Files.txt')
responsecontent = response.text
print(responsecontent)
for file in responsecontent.split("\n"):
    file = file.replace("b'", "")
    file = file.replace("'", "")
    file = file.replace(r"\n", "")
    if file == "":
        pass
    elif "Logged.txt" == file:
        pass
    else:
        url = f'https://raw.githubusercontent.com/Charonum/JSCode/main/code/windows/{file}'
        print(f"Fetching {url}")
        wget.download(url)


print("Cleaning Up...")

os.remove("Version.txt")
os.rename("Version (1).txt", "Version.txt")

user_file = open("Logged.txt", "r")
user = user_file.read()
user_file.close()

print("Done!")
print("Update Complete")

if user == "guest3392":
    print("User not logged in. Redirecting...")
    os.remove("Logged.txt")
    new_logged = open("Logged.txt", "w")
    new_logged.close()
    os.system("JSMain.pyw")
    quit()
elif user == "":
    print("User not logged in. Redirecting...")
    os.remove("Logged.txt")
    new_logged = open("Logged.txt", "w")
    new_logged.close()
    os.system("JSMain.pyw")
    quit()
else:
    print(f"Redirecting {user} to menu.")
    os.system("ServerSelect.pyw")
    quit()
