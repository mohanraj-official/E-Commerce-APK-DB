from flask import Blueprint, jsonify
from models.product_model import get_all_products

products_bp = Blueprint('products_bp', __name__)

@products_bp.route('/', methods=['GET'])
def products():
    data = get_all_products()
    return jsonify(data)
