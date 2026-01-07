from fastapi import FastAPI
import json
import pathlib

app = FastAPI()

userList = []

messages = [
    {}
]


class Users:
    def __init__(self, name, password):
        self.name = name
        self.password = password


@app.get('/con_check')
def check_con():
    return {'connection': "hej"}


@app.post('/sign_up')
async def createUser(user: dict):
    userList.append(Users(user["name"], user["password"]))
    await save_userlist(user)
    return user


async def save_userlist(user):
    with open(f'{user['name']}.json','w') as file:
        json.dump(user, file)


@app.post('/send_message')
async def send_message(message: dict):
    with open(f'message_{message['sender']}_{message['reciever']}','w') as file:
        f = json.load(file)
        file.seek(0)
        json.dump(message['message'],f, file)
        return 'Message sent successfully'


@app.get('/recieve_message')
async def recieve_message(dic: dict):
    directory = pathlib.Path(f"message_{dic['sender']}_{dic['reciever']}")
    with open(directory,'r') as file:
        data = json.load(file)[1]
        return data
    



if __name__ == "__main__":
    import uvicorn; from pathlib import Path
    uvicorn.run(f'{Path(__file__).resolve().stem}:app', host="0.0.0.0", port=8000, reload=True)