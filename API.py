from fastapi import FastAPI
import json

app = FastAPI()

userList = []

messages = [
    {}
]


class Users:
    def __init__(self, name, password):
        self.name = name
        self.password = password


@app.post('/sign up')
async def createUser(user: dict):
    userList.append(Users(user["name"], user["password"]))
    await save_userlist(user)
    return user


async def save_userlist(user):
    with open('users.json','w') as file:
        json.dump(user, file)

@app.post('/send_message')
async def send_message(user1: dict, user2: dict, message: str):
    with open(f'message_{user1['name']}_{user2['name']}','w') as file:
        json.dump(message, file)


if __name__ == "__main__":
    import uvicorn; from pathlib import Path
    uvicorn.run(f'{Path(__file__).resolve().stem}:app', host="0.0.0.0", port=8000, reload=True)