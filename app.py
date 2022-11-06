from flask import Flask
from flask import request
from flask import jsonify
from db.db_manager import load_orders, save_new_order
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/v1/orders', methods=['POST'])
def new_order():
    req_json = request.json

    # Here the code

    return None


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
