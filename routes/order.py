from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic_schemas import Order as OrderSchema, OrderItem as OrderItemSchema
from database import get_db
from crud.orders import create_order, create_final_order
from auth import validate


order_router = APIRouter()

@order_router.post("/create_order_item", dependencies=[Depends(validate)])
def create_order_item_endpoint(order_item: OrderItemSchema, db: Session = Depends(get_db)):
    return create_order(order_item, db)

@order_router.post("/create_final_order", dependencies=[Depends(validate)])
def create_final_order_endpoint(order: OrderSchema, db: Session = Depends(get_db)):
    return create_final_order(order, db)