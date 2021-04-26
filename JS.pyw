import json
import threading
import time
import requests

filee = open("Logged.txt", "r")
user = filee.read()
filee.close()

if "guest3392" in user:
    fileee = open("Logged.txt", "w")
    fileee.write("")
    fileee.close()

API_KEY = "tdckrMO6mGTD"
PROJECT_TOKEN = "t7mCATFxt4_e"
RUN_TOKEN = "tcG0Mpa3LYYT"


class Data:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            "api_key": self.api_key
        }
        self.data = self.get_data()

    def get_data(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/last_ready_run/data',
                                params=self.params)
        data = json.loads(response.text)
        return data

    def get_version(self):
        data = self.data['Version']

        return data

    def update_data(self):
        response = requests.post(f'https://www.parsehub.com/api/v2/projects/{self.project_token}/run',
                                 params=self.params)

        def poll():
            time.sleep(0.1)
            old_data = self.data
            while True:
                new_data = self.get_data()
                if new_data != old_data:
                    self.data = new_data
                    print("Data updated")
                    break
                time.sleep(5)

        t = threading.Thread(target=poll)
        t.start()


def start():
    data = Data(API_KEY, PROJECT_TOKEN)
    data.update_data()
    file = open("Version.txt", "r")
    version = file.read()
    file.close()
    file2 = open("Logged.txt", "r")
    user = file2.read()
    file2.close()

    if data.get_version() == version:
        if user == "":
            import os
            os.system("JSMain.pyw")
            quit()
        import os
        os.system('ServerSelect.pyw')
        quit()
    else:
        import os
        os.chdir("Stiff_Files")
        os.system("setup.py")


start()
