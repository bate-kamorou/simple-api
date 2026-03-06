from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def sayhello():
    return {"message" : "Hello, World!"}