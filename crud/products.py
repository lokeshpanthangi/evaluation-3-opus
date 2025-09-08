from models import Product, User


#check if the id is vendor or not
def check_vendor(vendor_id, db):
    vendor = db.query(User).filter(User.id == vendor_id, User.user_type == 'vendor').first()
    if vendor:
        return True
    return False





def add_product(product, db):
    if not check_vendor(product.vendor_id, db):
        return {"error": "Invalid vendor ID"}
    new_product = Product(
        vendor_id=product.vendor_id,
        name=product.name,
        category=product.category,
        price=product.price,
        min_quantity=product.min_quantity,
        stock=product.stock
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_products(db):
    return db.query(Product).all()

def get_product_by_id(product_id, db):
    return db.query(Product).filter(Product.id == product_id).first()

