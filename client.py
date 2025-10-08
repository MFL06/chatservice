import requests

API_URL = "http://(server name)"

def opret_bruger():
    print("=== Opret ny bruger ===")
    brugernavn = input("Brugernavn: ")

    data = {
        "username": brugernavn,
    }

    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 201:
            print("Bruger oprettet!")
        else:
            print(f"Fejl: {response.status_code} - {response.text}")
    except requests.exceptions.RequestException as e:
        print("Kunne ikke forbinde til serveren:", e)

if __name__ == "__main__":
    opret_bruger()
