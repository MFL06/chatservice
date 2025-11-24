import requests

API_URL = "http://10.74.68.175:8000"

def opret_bruger():
    print("=== Opret ny bruger ===")
    name = input("name: ")
    password = input("password:")

    try:
        response = requests.post(f"{API_URL}/sign up", json={"name": name, "password": password})
        if response.status_code == 200:
            print("Bruger oprettet!",response.text)
        else:
            print(f"Fejl: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print("Kunne ikke forbinde til serveren:", e)

if __name__ == "__main__":
    opret_bruger()
