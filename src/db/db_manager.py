import csv


def load_orders():
    orders = []
    with open('db/orders.csv', 'r') as orders_file:
        rows = csv.DictReader(orders_file)

        for row in rows:
            orders.append()

        return orders


def save_new_order(order):
    with open('src/db/orders.csv', 'a') as orders_file:
        header = ["order_id", "user", "address", "phone_number", "shopping_cart"]

        writer = csv.DictWriter(orders_file, fieldnames=header)

        if orders_file.tell() == 0:
            writer.writeheader()

        writer.writerow(order)
