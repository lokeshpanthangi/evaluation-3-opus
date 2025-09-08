from models import Order
from pydantic_schemas import Order as OrderSchema



def create_orders(order: OrderSchema, db):
    new_order = Order(
        buyer_id=order.buyer_id,
        total_amount=order.total_amount,
        discount_percent=order.discount_percent,
        final_amount=order.final_amount
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order    