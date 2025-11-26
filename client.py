import requests

API_URL = "http://10.74.68.175:8000"

user_name = False


class Bruger:
    def __init__(self, name, password):
        self.name = name
        self.password = password

def opret_bruger():
    print("=== Opret ny bruger ===")
    name = input("name: ")
    password = input("password: ")

    try:
        response = requests.post(f"{API_URL}/sign up", json={"name": name, "password": password})
        if response.status_code == 200:
            print("Bruger oprettet!", response.text)
            global user_name
            user_name = name
            print(user_name)
        else:
            print(f"Fejl: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print("Kunne ikke forbinde til serveren:", e)

if __name__ == "__main__":
    bruger = opret_bruger()

    if bruger:
        print("Bruger objekt gemt:")
        print("Navn:", bruger.name)
        print("Password:", bruger.password)



    
def send_message():
    print("=== Send en besked ===")
    message = input("message: ")
    reciever = input("modtager: ")
    
    try:
        response = requests.post(f"{API_URL}/send_message", json={f'message': message, 'reciever': reciever, 'sender':user_name})
        if response.status_code == 200:
            print("Besked sendt", response.text)
        else:
            print(f"Fejl: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print("Kunne ikke forbinde til serveren:", e)

if user_name != False:
    send_message()