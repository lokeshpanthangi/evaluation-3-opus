from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class User(BaseModel):
    username: str
    email: str
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
    total_amount: float
    discount_percent: float
    final_amount: float


class OrderItem(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int
    unit_price: float
    subtotal: float




