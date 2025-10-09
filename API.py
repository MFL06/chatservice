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
def createUser(name: str, password: str):
    userList.append(Users(name, password))


if __name__ == "__main__":
    import uvicorn; from pathlib import Path
    uvicorn.run(f'{Path(__file__).resolve().stem}:app', host="0.0.0.0", port=8000, reload=True)