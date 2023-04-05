import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from crud import (
    create_product,
    delete_product,
    get_product,
    get_products,
)
from models import Product

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000/"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/products")
def all():
    return get_products()


@app.post("/products")
def create(product: Product):
    return create_product(product)


@app.get("/products/{pk}")
def get(pk: str):
    return get_product(pk)


@app.delete("/products/{pk}")
def delete(pk: str):
    return delete_product(pk)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
