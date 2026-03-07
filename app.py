from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def sayhello():
    return {"message" : "Hello, World!"}


# greeting  endpoint (query parameter)
@app.get("/greet")
def greetings(name:str):
    return {"message": f"hello {name} nice to meet you 🤝"}

# add endpoint (multi query parameters)
@app.get("/add")
def add_nums(a:float, b:float):
    result = a + b
    return {"Response" : f"Sum of a:{a} and b:{b} is equals to: {result}"}

# add a post enpoint 
class Nums(BaseModel):
    a:float
    b:float

@app.post("/add-json")
def multiply_json(numbers: Nums):
    result = numbers.a * numbers.b
    return {"result": result}
