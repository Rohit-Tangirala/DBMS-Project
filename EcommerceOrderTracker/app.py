from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import get_db_connection

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/')
def index():
    return render_template('index.html')

# ---------------- PRODUCTS ----------------
@app.route('/products')
def products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return render_template('products.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form['name']
    price = request.form['price']
    stock = request.form['stock']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)", (name, price, stock))
    conn.commit()
    conn.close()
    flash("Product added successfully!")
    return redirect(url_for('products'))

# ---------------- CUSTOMERS ----------------
@app.route('/customers')
def customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return render_template('customers.html', customers=customers)

@app.route('/add_customer', methods=['POST'])
def add_customer():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
    conn.commit()
    conn.close()
    flash("Customer added successfully!")
    return redirect(url_for('customers'))

# ---------------- ORDERS ----------------
@app.route('/orders')
def orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT o.order_id, c.name AS customer, o.order_date, o.total_amount
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
    """)
    orders = cursor.fetchall()
    conn.close()
    return render_template('orders.html', orders=orders)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
