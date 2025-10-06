from fastapi import FastAPI

app = FastAPI()

userList = []

messageList = []

class Users:
    def __init__(self, name):
        self.name = name
    
    def createUser(name):
        userList.append(Users(name))













if __name__ == "__main__":
    import uvicorn; from pathlib import Path
    uvicorn.run(f'{Path(__file__).resolve().stem}:app', host="0.0.0.0", port=8000, reload=True)