from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def sayhello():
    return {"message" : "Hello, World!"}


# greeting  endpoint (query parameter)
@app.get("/greet")
def greetings(name:str):
    return {"message": f"hello {name} nice to meet you 🤝"}

# use pydantic basemodel for type validation


# add endpoint (multi query parameters)
@app.get("/add")
def add_nums(a:float, b:float):
    result = a + b
    return {"Response" : f"Sum of a:{a} and b:{b} is equals to: {result}"}
