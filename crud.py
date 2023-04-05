from models import Product


def format(pk: str):
    product = get_product(pk)

    return {
        "id": product.pk,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
    }


def get_products():
    return [format(pk) for pk in Product.all_pks()]


def get_product(pk: str):
    product = Product.get(pk)
    return product


def create_product(product: Product):
    new_product = product.save()
    return new_product


def delete_product(pk: str):
    product = Product.delete(pk)
    return product
