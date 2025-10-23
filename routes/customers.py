from flask import Blueprint, jsonify
from models.customer_model import get_all_customers

customers_bp = Blueprint('customers_bp', __name__)

@customers_bp.route('/', methods=['GET'])
def customers():
    data = get_all_customers()
    return jsonify(data)
