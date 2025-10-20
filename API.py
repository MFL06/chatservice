from fastapi import FastAPI


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
    return userList


if __name__ == "__main__":
    import uvicorn; from pathlib import Path
    uvicorn.run(f'{Path(__file__).resolve().stem}:app', host="0.0.0.0", port=8000, reload=True)