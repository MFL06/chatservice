import requests

API_URL = "http://10.74.68.152:8000"



user_name = False

value = True

process = False

class Bruger:
    def __init__(self, name, password):
        self.name = name
        self.password = password

def opret_bruger():
    response1 = requests.get(f"{API_URL}/con_check", 's')
    if response1.status_code == 200:
        print(response1.text)
    print("=== Opret ny bruger ===")
    name = input("name: ")
    password = input("password: ")
    response = requests.post(f"{API_URL}/sign_up", json={"name": name, "password": password})
    if response.status_code == 200:
        print("Bruger oprettet!", response.text)
        global user_name
        user_name = name
        print(user_name)
    else:
        print(f"Fejl: {response.status_code} - {response.text}")


#if __name__ == "__main__":
 #   opret_bruger()




    
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
    global process
    process = False






def recieve_message():
    sender = input("Who do you want to get message from? ")
    reciever = user_name

    response = requests.get(f"{API_URL}/recieve_message", json={f'sender': sender, 'reciever': reciever})
    if response.status_code == 200:
        print(response.text)
    else:
        print('Der opstod en fejl!')
    global process
    process = False



#while True:
 #   action = input("Tryk 'r' for at få beskeder \n Tryk 's' for at sende besked \n Tryk 'c' for at lukke programmet\n")
  #  if process == False:
   #     if action == 'r':
    #        recieve_message()
     #   if action == 's':
      #      send_message()
       # if action == 'c':
        #    break
