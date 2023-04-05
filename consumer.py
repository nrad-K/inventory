import time

from redis import ResponseError

from database import redis
from models import Product
from producer import send_data

key = "order_completed"
group = "inventory-group"


while True:
    print("Checking Order Completed....")
    try:
        redis.xgroup_create(name=key, groupname=group)
    except ResponseError as e:
        print(e)

    try:
        # response = redis.xread(streams={key: last_job_id}, count=1, block=5000)
        responses = redis.xreadgroup(
            groupname=group, consumername="c", count=1, block=5000, streams={key: ">"}
        )

        if len(responses) == 0:
            print("Nothing to do right now, sleeping....")
            time.sleep(5)
            continue

        for response in responses:
            result = response[1][0][1]
            print(result)

            order_id = result["product_id"]
            order_quantity = result["quantity"]

            product = Product.get(order_id)
            if product.quantity < int(order_quantity):
                send_data("refund_order", result)
                continue

            # Update Product
            product.quantity = product.quantity - int(order_quantity)
            product.save()
            time.sleep(5)

    except Exception as e:
        print(str(e))

    time.sleep(1)
