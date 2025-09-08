from fastapi import FastAPI
from models import Base
from database import engine
from routes.user import user_router
from routes.products import product_router
from routes.order import order_router

# FastAPI instance
app = FastAPI()
app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)

#SQL alchemy tables Creation
Base.metadata.create_all(bind=engine)