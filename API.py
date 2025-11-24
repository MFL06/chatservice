from fastapi import FastAPI
import csv

app = FastAPI()

userList = []

messages = [
    {}
]



class Users:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    
    async def ReceiveMsg(self, name, message: dict):
        print('skibidi')


@app.post('/messages')
def createUser(user: dict):
    userList.append(Users(user["name"], user["password"]))
    save_userlist(user)

def save_userlist(user):
    with open('data.csv','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(user)


if __name__ == "__main__":
    import uvicorn; from pathlib import Path
    uvicorn.run(f'{Path(__file__).resolve().stem}:app', host="0.0.0.0", port=8000, reload=True)