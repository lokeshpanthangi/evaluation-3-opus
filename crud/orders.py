from models import Order, OrderItem, Product
from pydantic_schemas import Order as OrderSchema, OrderItem as OrderItemSchema
from sqlalchemy import func


def calculate_discount(buyer_id: int, total_quantity: int, total_value: int, db):
    discount = 0.0
    # Quantity Bonus
    if total_quantity >= 1000:
        discount += 15.0
    elif total_quantity >= 500:
        discount += 10.0
    elif total_quantity >= 100:
        discount += 5.0

    # Value Bonus
    if total_value >= 10000:
        discount += 12.0
    elif total_value >= 5000:
        discount += 7.0
    elif total_value >= 1000:
        discount += 3.0

    # Loyalty Bonus
    previous_orders_count = db.query(Order).filter(Order.buyer_id == buyer_id).count()
    if previous_orders_count >= 4:
        discount += 5.0
    elif previous_orders_count >= 1:
        discount += 2.0

    return min(discount, 25.0)  # Cap the discount at 25%


def final_amount(total_amount: float, discount_percent: float) -> float:
    return total_amount * (1 - discount_percent / 100)



def create_order(order: OrderItemSchema, db):
    unit_price = db.query(Product.price).filter(Product.id == order.product_id).scalar()
    k = check_if_enough_stock(order, db)
    if not k:
        return {"error": "Insufficient stock for the product"}
    if not check_min_quantity(order, db):
        return {"error": "Order quantity is less than the minimum required quantity"}
    new_order = OrderItem(
        product_id=order.product_id,
        quantity=order.quantity,
        unit_price=unit_price,
        subtotal=order.quantity * unit_price
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order



def create_final_order(order: OrderSchema, db):
    total_amount=db.query(OrderItem).filter(OrderItem.id.in_(map(int, order.order_ids.split(',')))).with_entities(func.sum(OrderItem.subtotal)).scalar()
    total_quantity=db.query(OrderItem).filter(OrderItem.id.in_(map(int, order.order_ids.split(',')))).with_entities(func.sum(OrderItem.quantity)).scalar()
    discount_percent=calculate_discount(order.buyer_id, total_quantity, total_amount, db)
    new_order = Order(
        order_ids=order.order_ids,
        buyer_id=order.buyer_id,
        total_amount=total_amount,
        discount_percent=discount_percent,
        final_amount=final_amount(total_amount, discount_percent)
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order



# Validations NOW 



def check_if_enough_stock(order_item: OrderItemSchema, db):
    product = db.query(Product).filter(Product.id == order_item.product_id).first()
    if product and product.stock >= order_item.quantity:
        #subtract the stock
        product.stock -= order_item.quantity
        db.commit()
        return True
    return False


def check_min_quantity(order_item: OrderItemSchema, db):
    product = db.query(Product).filter(Product.id == order_item.product_id).first()
    if product and order_item.quantity >= product.min_quantity:
        return True
    return False