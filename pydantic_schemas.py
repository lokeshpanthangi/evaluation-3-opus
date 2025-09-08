from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
    password: str
    user_type: str
    company_name: str


class Product(BaseModel):
    vendor_id: int
    name: str
    category: str
    price: float  # Base price per unit
    min_quantity: int  # Minimum order quantity
    stock: int


class Order(BaseModel):
    buyer_id: int
    order_ids : str  # Comma-separated list of OrderItem IDs



class OrderItem(BaseModel):
    product_id: int
    quantity: int
    unit_price: float




