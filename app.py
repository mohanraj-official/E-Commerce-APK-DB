from flask import Flask, render_template
from routes.products import products_bp
from routes.customers import customers_bp
from routes.orders import orders_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(products_bp, url_prefix='/products')
app.register_blueprint(customers_bp, url_prefix='/customers')
app.register_blueprint(orders_bp, url_prefix='/orders')

# Simple frontend routing
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/view-products')
def view_products():
    return render_template('products.html')

@app.route('/view-customers')
def view_customers():
    return render_template('customers.html')

@app.route('/view-orders')
def view_orders():
    return render_template('orders.html')

if __name__ == "__main__":
    app.run(debug=True)
