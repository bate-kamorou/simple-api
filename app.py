from fastapi import FastAPI
from models import Nums
from service import add_nums, multiply_nums

app = FastAPI()

# health check endpoint 
@app.get("/health")
def health():
    return {"Status" : "API running..."}

# add endpoint (multi query parameters)
@app.post("/add")
def addition(nums:Nums):
    result = add_nums(nums.a, nums.b)
    return {"Response" : f"Sum of a:{nums.a} and b:{nums.b} is equals to: {result}"}

# add a post enpoint 
@app.post("/multiply")
def multiplication(nums:Nums):
    result  =   multiply_nums(nums.a, nums.b)
    return {"Result": result}