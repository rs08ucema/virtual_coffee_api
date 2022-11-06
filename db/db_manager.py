import csv


def load_orders():
    orders = []
    with open('src/db/orders.csv', 'r') as books_file:
        rows = csv.DictReader(books_file)

        for row in rows:
            orders.append()

        return orders


def save_new_order(order):
    with open('src/db/orders.csv', 'a') as orders_file:
        # Define headers
        header = []

        writer = csv.DictWriter(orders_file, fieldnames=header)

        if orders_file.tell() == 0:
            writer.writeheader()

        writer.writerow(order)
