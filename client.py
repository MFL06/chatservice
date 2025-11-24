import requests

API_URL = "http://10.74.68.175:8000"

class Bruger:
    def __init__(self, name, password):
        self.name = name
        self.password = password

def opret_bruger():
    print("=== Opret ny bruger ===")
    name = input("name: ")
    password = input("password:")

    try:
        response = requests.post(f"{API_URL}/sign up", json={"name": name, "password": password})
        if response.status_code == 200:
            print("Bruger oprettet!", response.text)
            return Bruger(name, password)
        else:
            print(f"Fejl: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print("Kunne ikke forbinde til serveren:", e)
        return None

if __name__ == "__main__":
    bruger = opret_bruger()

    if bruger:
        print("Bruger objekt gemt:")
        print("Navn:", bruger.name)
        print("Password:", bruger.password)
