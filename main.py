from fastapi import FastAPI,Request
from mockData import products

app=FastAPI()

@app.get("/")
def home():
    return "welcome fast api series !"

@app.get("/home")
def home(req,res):
    print(f"{req}")

@app.get("/products")
def get_products():
    return products

@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    for oneproduct in products:
        if oneproduct.get("id") == product_id:
            return oneproduct
    return {
        "error":"Product is not found"
    }

@app.get("/greet")
def greet_user(name:str,age:int):
    return{
        f"hello {name} welcome back age: {age}"
    }

@app.get("/greets")
def greets(request:Request):
 query_params= dict(request.query_params)
 return{
        "greet":query_params
    }