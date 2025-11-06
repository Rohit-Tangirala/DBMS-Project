
from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import get_db_connection

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return render_template("products.html", products=products)

@app.route("/customers")
def customers():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return render_template("customers.html", customers=customers)

@app.route("/orders")
def orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT o.*, c.name AS customer FROM orders o JOIN customers c ON o.customer_id = c.customer_id")
    orders = cursor.fetchall()

    for o in orders:
        cursor.execute("SELECT oi.*, p.name AS product_name FROM order_items oi JOIN products p ON oi.product_id = p.product_id WHERE oi.order_id = %s", (o["order_id"],))
        o["items"] = cursor.fetchall()

    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    conn.close()
    return render_template("orders.html", orders=orders, customers=customers, products=products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
