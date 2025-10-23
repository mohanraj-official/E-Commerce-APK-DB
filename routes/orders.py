from flask import Blueprint, jsonify, request
from models.order_model import get_all_orders, get_order_items
from utils.db_helper import get_connection

orders_bp = Blueprint('orders_bp', __name__)

@orders_bp.route('/', methods=['GET'])
def orders():
    data = get_all_orders()
    return jsonify(data)

@orders_bp.route('/<int:order_id>/items', methods=['GET'])
def order_items(order_id):
    data = get_order_items(order_id)
    return jsonify(data)

@orders_bp.route('/create', methods=['POST'])
def create_order():
    req = request.get_json()
    customer_id = req['customer_id']
    items = req['items']  # List of {product_id, qty, price}

    conn = get_connection()
    cur = conn.cursor()

    # Insert into ORDERS
    total = sum([i['qty'] * i['price'] for i in items])
    cur.execute("INSERT INTO ORDERS (CUSTOMER_ID, TOTAL_AMOUNT) VALUES (:1, :2) RETURNING ORDER_ID INTO :3",
                (customer_id, total, cur.var(cx_Oracle.NUMBER)))
    order_id = cur.lastrowid or cur.var(cx_Oracle.NUMBER).getvalue()

    # Insert into ORDER_ITEMS
    for item in items:
        cur.execute("INSERT INTO ORDER_ITEMS (ORDER_ID, PRODUCT_ID, QTY, PRICE) VALUES (:1, :2, :3, :4)",
                    (order_id, item['product_id'], item['qty'], item['price']))

    conn.commit()
    conn.close()
    return jsonify({"message": "Order created", "order_id": order_id})
