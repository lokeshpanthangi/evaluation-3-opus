from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    user_type = Column(String, nullable=False)  # 'vendor' or 'buyer'
    company_name = Column(String, nullable=False)
    created_at = Column(String, nullable=False, default=datetime.utcnow().isoformat())


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, nullable=False)  # Foreign key to User.id
    name = Column(String, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)
    price = Column(Integer, nullable=False)  # Base price per unit
    min_quantity = Column(Integer, nullable=False)  # Minimum order quantity
    stock = Column(Integer, nullable=False)  # Available stock
    created_at = Column(String, nullable=False, default=datetime.utcnow().isoformat())


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))  # Foreign key to Order.id
    product_id = Column(Integer, ForeignKey("products.id"))  # Foreign key to Product.id
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    subtotal = Column(Integer, nullable=False)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, nullable=False)  # Foreign key to User.id
    total_amount = Column(Integer, nullable=False)
    discount_percent = Column(Integer, nullable=False)
    final_amount = Column(Integer, nullable=False)
    created_at = Column(String, nullable=False, default=datetime.utcnow().isoformat())