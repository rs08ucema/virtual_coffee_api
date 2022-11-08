from flask import Flask
from flask import request
from flask import jsonify
from db.db_manager import load_orders, save_new_order
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/orders', methods=['POST'])
def new_order():
    req_json = request.json

    order_id = random.randint(1000, 10000000)
    req_json['order_id'] = order_id
    save_new_order(req_json)

    return {
        "order_id": str(order_id)
    }


@app.route('/api/v1/orders', methods=['GET'])
def get_orders():
    # Here the code
    return None


@app.route('/api/v1/orders/<order_id>', methods=['GET'])
def get_order_by_id():
    # Here the code
    return None


if __name__ == '__main__':
    app.run()
