from fastapi import APIRouter, Depends
from pydantic_schemas import Product as ProductSchema
from database import get_db
from crud.products import add_product, get_product_by_id, get_products
from sqlalchemy.orm import Session
from auth import validate


product_router = APIRouter()



@product_router.post("/add_product", dependencies=[Depends(validate)])
def add_product_endpoint(product: ProductSchema, db: Session = Depends(get_db)):
    return add_product(product, db)

@product_router.get("/products", dependencies=[Depends(validate)])
def get_products_endpoint(db: Session = Depends(get_db)):
    return get_products(db)

@product_router.get("/products/{product_id}", dependencies=[Depends(validate)])
def get_product_by_id_endpoint(product_id: int, db: Session = Depends(get_db)):
    return get_product_by_id(product_id, db)

