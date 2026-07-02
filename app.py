from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
import os
import mysql.connector
import pandas as pd
import numpy as np
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv
from sklearn.linear_model import LinearRegression
from twilio.rest import Client
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)
app.secret_key = "secret_key_123"


@app.context_processor
def inject_low_stock_info():
    if "role" in session and session["role"] == "Admin":
        try:
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True, buffered=True)

            cursor.execute(
                "SELECT COUNT(*) AS count FROM product WHERE quantity <= %s",
                (5,),
            )

            res = cursor.fetchone()

            cursor.close()
            conn.close()

            return {
                "low_stock_count": res["count"] if res else 0
            }

        except Exception:
            return {
                "low_stock_count": 0
            }

    return {
        "low_stock_count": 0
    }


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

ADMIN_PHONE = "+919487184056"
LOW_STOCK_THRESHOLD = 5


def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="homedb",
        port=3306,
    )


def send_alert_sms(message, mobile_number):
    try:
        if not mobile_number.startswith("+"):
            mobile_number = "+91" + mobile_number

        client = Client(
            TWILIO_ACCOUNT_SID,
            TWILIO_AUTH_TOKEN,
        )

        sent = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=mobile_number,
        )

        print(f"DEBUG Twilio Admin Alert SID: {sent.sid}")

        return {
            "status": "success",
            "message": "Admin alerted via Twilio",
        }

    except Exception as e:
        print(f"Error sending Twilio Alert: {e}")

        return {
            "status": "error",
            "message": str(e),
        }


@app.route("/api/notify_admin_low_stock", methods=["POST", "GET"])
def notify_admin_low_stock():

    if "user" not in session or session.get("role") != "Admin":
        return jsonify(
            {
                "status": "error",
                "message": "Unauthorized",
            }
        ), 401

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)

        cursor.execute(
            """
            SELECT product_name, quantity
            FROM product
            WHERE quantity <= %s
            """,
            (LOW_STOCK_THRESHOLD,),
        )

        low_stock_items = cursor.fetchall()

        cursor.close()
        conn.close()

        if not low_stock_items:
            return jsonify(
                {
                    "status": "success",
                    "message": "No low stock items to report.",
                }
            )

        items_str = ", ".join(
            [
                f"{item['product_name']} ({item['quantity']})"
                for item in low_stock_items
            ]
        )

        alert_msg = (
            f"Alert Admin! Low stock items: {items_str}. "
            f"Please restock."
        )

        result = send_alert_sms(
            alert_msg,
            ADMIN_PHONE,
        )

        return jsonify(
            {
                "status": "success",
                "message": "Admin notified successfully!",
                "api_response": result,
            }
        )

    except Exception as e:
        return jsonify(
            {
                "status": "error",
                "message": str(e),
            }
        ), 500

@app.route("/")
@app.route("/index")
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()

    try:
        cursor.execute(
            """
            SELECT DISTINCT supplier_name
            FROM stock_in
            WHERE supplier_name IS NOT NULL
            AND supplier_name != ''
            """
        )

        suppliers_raw = cursor.fetchall()
        suppliers = [
            s["supplier_name"]
            for s in suppliers_raw
            if s["supplier_name"]
        ]

    except Exception:
        suppliers = []

    if not suppliers:
        suppliers = [
            "India Gate",
            "Heritage",
            "Kellogg's",
            "Nestle",
            "Aashirvaad",
            "Amul",
            "Britannia",
            "Patanjali",
        ]

    cursor.close()
    conn.close()

    return render_template(
        "index.html",
        products=products,
        suppliers=suppliers,
    )


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)

        cursor.execute(
            """
            SELECT *
            FROM content
            WHERE Email = %s
            AND Password = %s
            """,
            (email, password),
        )

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user:
            session["user"] = user["Email"]
            session["user_id"] = user["id"]
            session["role"] = user["Role"] if user["Role"] else "User"

            flash("Login Successful!", "success")

            return redirect(
                url_for(
                    "viewproduct"
                    if session["role"] == "Admin"
                    else "index"
                )
            )

        flash("Invalid Credentials!", "danger")
        return redirect(url_for("login_page"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register_logic():
    if request.method == "GET":
        return render_template("register.html")

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    phone = request.form.get("phone")
    password = request.form.get("password")

    full_name = f"{fname} {lname}"
    role = "Admin" if email == "admin@gmail.com" else "User"

    conn = get_db_connection()
    cursor = conn.cursor(buffered=True)

    try:
        cursor.execute(
            """
            INSERT INTO content
            (Name, Email, Password, Phone, Role)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                full_name,
                email,
                password,
                phone,
                role,
            ),
        )

        conn.commit()

        flash(
            "Registration Successful! Please Login!",
            "success",
        )

        return redirect(url_for("login_page"))

    except Exception as e:
        flash(f"Error: {str(e)}", "danger")
        return redirect(url_for("register_logic"))

    finally:
        cursor.close()
        conn.close()


@app.context_processor
def inject_categories():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)

        cursor.execute("SELECT * FROM category")
        categories = cursor.fetchall()

        cursor.close()
        conn.close()

        return dict(nav_categories=categories)

    except Exception as e:
        print(f"Error in context processor: {e}")
        return dict(nav_categories=[])


@app.route("/category")
def category_page():
    if "user" not in session or session.get("role") != "Admin":
        return redirect(url_for("login_page"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT * FROM category")
    categories = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "category.html",
        categories=categories,
    )


@app.route("/add_category", methods=["POST"])
def add_category():
    if "user" not in session or session.get("role") != "Admin":
        return redirect(url_for("login_page"))

    name = request.form.get("name")
    description = request.form.get("description")
    image = request.files.get("image")

    filename = (
        secure_filename(image.filename)
        if image
        else "default_cat.jpg"
    )

    if image:
        upload_path = os.path.join(
            BASE_DIR,
            "static/uploads",
        )

        if not os.path.exists(upload_path):
            os.makedirs(upload_path)

        image.save(
            os.path.join(
                upload_path,
                filename,
            )
        )

    conn = get_db_connection()
    cursor = conn.cursor(buffered=True)

    cursor.execute(
        """
        INSERT INTO category
        (name, description, image)
        VALUES (%s, %s, %s)
        """,
        (
            name,
            description,
            filename,
        ),
    )

    conn.commit()

    cursor.close()
    conn.close()

    flash(
        "Category added successfully!",
        "success",
    )

    return redirect(url_for("category_page"))

@app.route('/edit_category/<int:id>')
def edit_category(id):
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login_page'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT * FROM category WHERE id = %s", (id,))
    category = cursor.fetchone()

    cursor.close()
    conn.close()

    if not category:
        flash("Category not found!", "danger")
        return redirect(url_for('category_page'))

    return render_template("edit_category.html", category=category)


@app.route('/update_category/<int:id>', methods=['POST'])
def update_category(id):
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login_page'))

    name = request.form.get('name')
    description = request.form.get('description')
    image = request.files.get('image')

    conn = get_db_connection()
    cursor = conn.cursor(buffered=True)

    if image and image.filename:
        filename = secure_filename(image.filename)

        upload_path = os.path.join(BASE_DIR, "static/uploads")
        os.makedirs(upload_path, exist_ok=True)

        image.save(os.path.join(upload_path, filename))

        cursor.execute(
            """
            UPDATE category
            SET name=%s, description=%s, image=%s
            WHERE id=%s
            """,
            (name, description, filename, id)
        )
    else:
        cursor.execute(
            """
            UPDATE category
            SET name=%s, description=%s
            WHERE id=%s
            """,
            (name, description, id)
        )

    conn.commit()
    cursor.close()
    conn.close()

    flash("Category updated successfully!", "success")
    return redirect(url_for('category_page'))


@app.route('/delete_category/<int:id>')
def delete_category(id):
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login_page'))

    conn = get_db_connection()
    cursor = conn.cursor(buffered=True)

    cursor.execute("DELETE FROM category WHERE id = %s", (id,))

    conn.commit()
    cursor.close()
    conn.close()

    flash("Category deleted successfully!", "success")
    return redirect(url_for('category_page'))


@app.route('/add_product_page')
def add_product_page():
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login_page'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT * FROM category")
    categories = cursor.fetchall()

    cursor.execute("SELECT * FROM product ORDER BY id DESC")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "addproducts.html",
        categories=categories,
        products=products
    )


@app.route('/viewproduct')
def viewproduct():
    if 'user' not in session:
        return redirect(url_for('login_page'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT * FROM product")
    products = cursor.fetchall()

    sql_feedback = """
        SELECT
            f.*,
            c.Name AS user_name,
            p.product_name
        FROM feedback f
        LEFT JOIN content c
            ON f.user_id = c.id
        LEFT JOIN product p
            ON f.product_id = p.id
        ORDER BY f.id DESC
    """
    cursor.execute(sql_feedback)
    feedbacks = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) AS count FROM content")
    total_users = cursor.fetchone()['count']

    total_products_count = len(products)

    cursor.execute("SELECT COUNT(*) AS count FROM orders")
    total_orders = cursor.fetchone()['count']

    cursor.execute("SELECT COUNT(*) AS count FROM orders WHERE status = 'Pending'")
    pending_orders = cursor.fetchone()['count']

    cursor.execute("SELECT COUNT(*) AS count FROM category")
    total_categories = cursor.fetchone()['count']

    try:
        cursor.execute("""
            SELECT COUNT(DISTINCT supplier_name) AS count
            FROM stock_in
            WHERE supplier_name IS NOT NULL
            AND supplier_name != ''
        """)
        total_suppliers = cursor.fetchone()['count']
    except Exception:
        total_suppliers = 0

    cursor.execute(
        "SELECT COUNT(*) AS count FROM product WHERE quantity <= %s",
        (LOW_STOCK_THRESHOLD,)
    )
    low_stock_count_val = cursor.fetchone()['count']

    sql_recent_orders = """
        SELECT
            o.*,
            c.Name AS customer_name,
            c.Email AS customer_email
        FROM orders o
        JOIN content c
            ON o.user_id = c.id
        ORDER BY o.order_date DESC
        LIMIT 5
    """
    cursor.execute(sql_recent_orders)
    recent_orders = cursor.fetchall()

    cursor.execute(
        "SELECT * FROM product WHERE quantity <= %s",
        (LOW_STOCK_THRESHOLD,)
    )
    low_stock_alerts = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template(
        "viewproduct.html",
        products=products,
        feedbacks=feedbacks,
        low_stock_alerts=low_stock_alerts,
        total_users=total_users,
        total_products=total_products_count,
        total_orders=total_orders,
        pending_orders=pending_orders,
        total_categories=total_categories,
        total_suppliers=total_suppliers,
        low_stock_count_val=low_stock_count_val,
        recent_orders=recent_orders
    )


@app.route('/stockin_page')
def stockin_page():
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login_page'))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT id, product_name FROM product")
    products = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("stockin.html", products=products)


@app.route('/save_stockin', methods=['POST'])
def save_stockin():
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login_page'))

    product_id = request.form.get('product_id')
    supplier_name = request.form.get('supplier_name')
    supplier_address = request.form.get('supplier_address')
    quantity = int(request.form.get('quantity'))
    price = float(request.form.get('price'))

    total_amount = quantity * price

    conn = get_db_connection()
    cursor = conn.cursor(buffered=True)

    try:
        cursor.execute(
            """
            INSERT INTO stock_in
            (
                product_id,
                supplier_name,
                supplier_address,
                quantity,
                price,
                total_amount,
                date_added
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                product_id,
                supplier_name,
                supplier_address,
                quantity,
                price,
                total_amount,
                datetime.now()
            )
        )
        
               cursor.execute(
            "UPDATE product SET quantity = quantity + %s WHERE id = %s",
            (quantity, product_id)
        )

        conn.commit()
        flash("Stock updated successfully!", "success")

    except Exception:
        conn.rollback()

        try:
            cursor.execute(
                """
                INSERT INTO stock_in
                (
                    product_id,
                    supplier_name,
                    supplier_address,
                    quantity,
                    price,
                    total_amount
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    product_id,
                    supplier_name,
                    supplier_address,
                    quantity,
                    price,
                    total_amount
                )
            )

            cursor.execute(
                "UPDATE product SET quantity = quantity + %s WHERE id = %s",
                (quantity, product_id)
            )

            conn.commit()
            flash("Stock updated successfully!", "success")

        except Exception as inner_e:
            flash(f"Error updating stock: {str(inner_e)}", "danger")

    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('viewproduct'))


@app.route('/api/product/<int:id>')
def api_product_detail(id):
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute("SELECT * FROM product WHERE id = %s", (id,))
    product = cursor.fetchone()

    cursor.close()
    conn.close()

    if product:
        return jsonify(product)

    return jsonify({"error": "Product not found"}), 404


@app.route('/api/low_stock_products')
def api_low_stock_products():
    if 'role' not in session or session['role'] != 'Admin':
        return jsonify({"error": "Admin access required"}), 403

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)

        cursor.execute(
            """
            SELECT
                id,
                product_name,
                quantity,
                category,
                image,
                restock_level
            FROM product
            WHERE quantity <= %s
            ORDER BY quantity ASC
            """,
            (LOW_STOCK_THRESHOLD,)
        )

        products = cursor.fetchall()

        cursor.close()
        conn.close()

        return jsonify(products)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/recent_stockin')
def api_recent_stockin():
    if 'role' not in session or session['role'] != 'Admin':
        return jsonify({"error": "Admin access required"}), 403

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    try:
        cursor.execute(
            """
            SELECT
                s.*,
                p.product_name
            FROM stock_in s
            JOIN product p
                ON s.product_id = p.id
            ORDER BY s.id DESC
            LIMIT 10
            """
        )

    except Exception:
        cursor.execute(
            "SELECT * FROM stock_in ORDER BY id DESC LIMIT 10"
        )

    stocks = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(stocks)


@app.route('/save_product', methods=['POST'])
def save_product():
    product_name = request.form.get('product_name')
    category = request.form.get('category')
    price = request.form.get('price')
    quantity = request.form.get('quantity')

    original_price = request.form.get('original_price')
    original_price = original_price if original_price else None

    restock_level = request.form.get('restock_level', 10)
    unit = request.form.get('unit', '1 Kg')
    description = request.form.get('description', '')
    image = request.files['image']

    filename = secure_filename(image.filename) if image else "default.jpg"

    if image:
        upload_path = os.path.join(BASE_DIR, "static/uploads")
        os.makedirs(upload_path, exist_ok=True)

        image.save(os.path.join(upload_path, filename))

    conn = get_db_connection()
    cursor = conn.cursor(buffered=True)

    cursor.execute(
        """
        INSERT INTO product
        (
            product_name,
            category,
            price,
            quantity,
            restock_level,
            image,
            original_price,
            unit,
            description
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            product_name,
            category,
            price,
            quantity,
            restock_level,
            filename,
            original_price,
            unit,
            description
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    flash(f"Product '{product_name}' added successfully!", "success")

    return redirect(url_for('add_product_page'))


@app.route('/inline_update_product', methods=['POST'])
def inline_update_product():
    if 'user' not in session or session.get('role') != 'Admin':
        return jsonify(
            {
                "status": "error",
                "message": "Unauthorized"
            }
        ), 401

    data = request.get_json()

    pid = data.get('id')
    quantity = data.get('quantity')
    restock_level = data.get('restock_level')

    try:
        conn = get_db_connection()
        cursor = conn.cursor(buffered=True)

        cursor.execute(
            """
            UPDATE product
            SET quantity = %s,
                restock_level = %s
            WHERE id = %s
            """,
            (quantity, restock_level, pid)
        )

        conn.commit()

        if int(quantity) <= LOW_STOCK_THRESHOLD:
            try:
                cursor.execute(
                    "SELECT product_name FROM product WHERE id = %s",
                    (pid,)
                )

                p_name = cursor.fetchone()[0]

                alert_msg = (
                    f"Alert Admin! {p_name} stock manually updated "
                    f"and is low. Only {quantity} units left."
                )

                send_alert_sms(alert_msg, ADMIN_PHONE)

            except Exception:
                pass

                cursor.close()
        conn.close()

        return jsonify({"status": "success"})

    except Exception as e:
        return jsonify(
            {
                "status": "error",
                "message": str(e)
            }
        ), 500


@app.route('/update_product', methods=['POST'])
def update_product():
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login_page'))

    pid = request.form.get('id')
    product_name = request.form.get('product_name')
    category = request.form.get('category')
    price = request.form.get('price')
    quantity = request.form.get('quantity')

    original_price = request.form.get('original_price')
    original_price = original_price if original_price else None

    unit = request.form.get('unit', '1 Kg')
    description = request.form.get('description', '')
    image = request.files.get('image')

    conn = get_db_connection()
    cursor = conn.cursor(buffered=True)

    if image and image.filename:
        filename = secure_filename(image.filename)

        upload_path = os.path.join(BASE_DIR, "static/uploads")
        os.makedirs(upload_path, exist_ok=True)

        image.save(os.path.join(upload_path, filename))

        cursor.execute(
            """
            UPDATE product
            SET
                product_name = %s,
                category = %s,
                price = %s,
                quantity = %s,
                image = %s,
                original_price = %s,
                unit = %s,
                description = %s
            WHERE id = %s
            """,
            (
                product_name,
                category,
                price,
                quantity,
                filename,
                original_price,
                unit,
                description,
                pid
            )
        )

    else:
        cursor.execute(
            """
            UPDATE product
            SET
                product_name = %s,
                category = %s,
                price = %s,
                quantity = %s,
                original_price = %s,
                unit = %s,
                description = %s
            WHERE id = %s
            """,
            (
                product_name,
                category,
                price,
                quantity,
                original_price,
                unit,
                description,
                pid
            )
        )

    conn.commit()

    try:
        if int(quantity) <= LOW_STOCK_THRESHOLD:
            alert_msg = (
                f"Alert Admin! {product_name} stock updated and "
                f"is low. Only {quantity} units left."
            )

            send_alert_sms(alert_msg, ADMIN_PHONE)

    except Exception:
        pass

    cursor.close()
    conn.close()

    return redirect(url_for('viewproduct'))


@app.route('/editproduct/<int:id>')
def edit_page(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)

    cursor.execute(
        "SELECT * FROM product WHERE id = %s",
        (id,)
    )

    product = cursor.fetchone()

    cursor.close()
    conn.close()
    return render_template("editproduct.html", product=product)

@app.route('/deleteproduct/<int:id>')
def delete_product(id):
    if 'user' not in session or session.get('role') != 'Admin':
        return redirect(url_for('login_page'))
        
    conn = get_db_connection()
    cursor = conn.cursor(buffered=True)
    try:
        # First delete from tables that have foreign keys pointing to this product
        cursor.execute("DELETE FROM stock_in WHERE product_id=%s", (id,))
        cursor.execute("DELETE FROM feedback WHERE product_id=%s", (id,))
        
        # Now delete the actual product
        cursor.execute("DELETE FROM product WHERE id=%s", (id,))
        conn.commit()
        flash("Product deleted successfully!", "success")
    except Exception as e:
        conn.rollback()
        flash(f"Error deleting product: {str(e)}", "danger")
    finally:
        cursor.close()
        conn.close()
    
    # Redirect back to the page the user was on (e.g., the products list)
    return redirect(request.referrer or url_for('viewproduct'))

# --- USER ROUTES (Shopping) ---

@app.route('/product/<int:id>')
def product_detail(id):
    if 'user_id' not in session: return redirect(url_for('login_page'))
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    
    cursor.execute("SELECT * FROM product WHERE id = %s", (id,))
    product = cursor.fetchone()

    # JOIN feedback with content to get the user's name
    query = """
        SELECT f.*, c.Name 
        FROM feedback f 
        JOIN content c ON f.user_id = c.id 
        WHERE f.product_id = %s 
        ORDER BY f.id DESC
    """
    cursor.execute(query, (id,))
    feedbacks = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('product_detail.html', product=product, feedbacks=feedbacks)



@app.route('/submit_feedback/<int:pid>', methods=['POST'])
def submit_feedback(pid):
    if 'user_id' not in session: return redirect(url_for('login_page'))
    description = request.form.get('description')
    rating = request.form.get('rating', 5) # Default to 5 if not provided
    user_id = session.get('user_id')
    if description:
        conn = get_db_connection()
        cursor = conn.cursor(buffered=True)
        cursor.execute("INSERT INTO feedback (user_id, product_id, description, rating) VALUES (%s, %s, %s, %s)", 
                     (user_id, pid, description, rating))
        conn.commit()
        cursor.close()
        conn.close()
    return redirect(url_for('product_detail', id=pid))

@app.route('/feedback_page')
def feedback_page():
    product_id = request.args.get('product_id')
    return render_template("feedback.html", product_id=product_id)

@app.route('/save_feedback', methods=['POST'])
def save_feedback():
    if 'user_id' not in session:
        return jsonify({"status": "error", "message": "Login required"})
    
    product_id = request.form.get('product_id')
    rating = request.form.get('rating')
    description = request.form.get('description')
    user_id = session.get('user_id')

    try:
        conn = get_db_connection()
        cursor = conn.cursor(buffered=True)
        cursor.execute("INSERT INTO feedback (user_id, product_id, rating, description) VALUES (%s, %s, %s, %s)", 
                     (user_id, product_id, rating, description))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "message": "Feedback submitted"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/place_order', methods=['POST'])
def place_order():
    if 'user_id' not in session:
        return jsonify({"status": "error", "message": "Login required"})

    try:
        data = request.get_json()
        user_id = session['user_id']
        product_id = data.get('product_id')
        item_name = data['item_name']
        qty = int(data['qty'])
        
        print(f"DEBUG: Processing order for User: {user_id}, Product ID: {product_id}, Item: {item_name}, Qty: {qty}")
        print(f"DEBUG: Customer Name: {data.get('customer_name')}, Phone: {data.get('customer_phone')}, Address: {data.get('address')}, Payment: {data.get('payment_method')}")
        print(f"DEBUG: Full data received: {data}")
        
        conn = get_db_connection()
        cursor = conn.cursor(buffered=True)
        
        # 1. Reduce stock quantity in 'product' table
        rows_affected = 0
        if product_id and str(product_id).strip() != "" and str(product_id).lower() != "undefined":
            print(f"DEBUG: Attempting update by ID: {product_id}")
            cursor.execute("UPDATE product SET quantity = quantity - %s WHERE id = %s", (qty, product_id))
            rows_affected = cursor.rowcount
            print(f"DEBUG: Rows affected by ID update: {rows_affected}")

        if rows_affected == 0:
            print(f"DEBUG: Falling back to update by Name: {item_name}")
            cursor.execute("UPDATE product SET quantity = quantity - %s WHERE product_name = %s", (qty, item_name))
            rows_affected = cursor.rowcount
            print(f"DEBUG: Rows affected by Name update: {rows_affected}")
        
        if rows_affected == 0:
            print(f"WARNING: No product found to reduce stock for {item_name} (ID: {product_id})")
        
        # 2. Insert into orders table
        sql = """
            INSERT INTO orders (
                order_id, user_id, item_name, qty, total_price, 
                customer_name, customer_email, customer_phone, address, payment_method, status
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data['order_id'], 
            user_id, 
            item_name, 
            qty, 
            data['total_price'],
            data.get('customer_name'),
            data.get('customer_email'),
            data.get('customer_phone'),
            data.get('address'),
            data.get('payment_method'),
            'Pending'
        )
        
        cursor.execute(sql, values)
        conn.commit()
        
        # --- LOW STOCK ALERT CHECK ---
        try:
            # Re-fetch quantity after update
            cursor.execute("SELECT product_name, quantity FROM product WHERE id = %s OR product_name = %s", (product_id, item_name))
            updated_product = cursor.fetchone()
            if updated_product:
                current_qty = updated_product[1] # Using index since it's not a dictionary cursor here
                p_name = updated_product[0]
                if current_qty <= LOW_STOCK_THRESHOLD:
                    alert_msg = f"Alert Admin! {p_name} stock romba low-a iruku. Only {current_qty} units left."
                    print(f"DEBUG: Triggering Low Stock SMS for {p_name}: {current_qty} left.")
                    send_alert_sms(alert_msg, ADMIN_PHONE)
        except Exception as alert_err:
            print(f"DEBUG: Low stock alert failed but not affecting order: {alert_err}")

        cursor.close()
        conn.close()
        return jsonify({"status": "success"})
    except Exception as e:
        print(f"Error in place_order: {e}")
        return jsonify({"status": "error", "message": str(e)})



@app.route('/my_orders')
def my_orders():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))
    
    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    
    # Orders-ai fetch pannuvom
    role = session.get('role', 'User')
    if role == 'Admin':
        cursor.execute("SELECT * FROM orders ORDER BY id DESC")
        orders = cursor.fetchall()
        cursor.execute("SELECT * FROM feedback ORDER BY id DESC")
        feedbacks = cursor.fetchall()
    else:
        cursor.execute("SELECT * FROM orders WHERE user_id = %s ORDER BY id DESC", (user_id,))
        orders = cursor.fetchall()
        cursor.execute("SELECT * FROM feedback WHERE user_id = %s ORDER BY id DESC", (user_id,))
        feedbacks = cursor.fetchall()


    
    cursor.close()
    conn.close()
    
    return render_template('my_orders.html', orders=orders, feedbacks=feedbacks)

@app.route('/order_details/<int:oid>')
def order_details(oid):
    if 'user_id' not in session:
        return redirect(url_for('login_page'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    cursor.execute("SELECT * FROM orders WHERE id = %s", (oid,))
    order = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if not order:
        flash("Order not found.", "danger")
        return redirect(url_for('my_orders'))
        
    return render_template('order_details.html', order=order)

@app.route('/update_order_status/<int:oid>', methods=['POST'])
def update_order_status(oid):
    if 'user' not in session or session.get('role') != 'Admin':
        return jsonify({"status": "error", "message": "Unauthorized"}), 401
    
    status = request.form.get('status', 'Delivered')
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(buffered=True)
        if status == 'Delivered':
            cursor.execute("UPDATE orders SET status = %s, order_trace = 'Delivered' WHERE id = %s", (status, oid))
        else:
            cursor.execute("UPDATE orders SET status = %s WHERE id = %s", (status, oid))
        conn.commit()
        cursor.close()
        conn.close()
        flash(f"Order #{oid} status updated to {status}.", "success")
        return redirect(request.referrer or url_for('my_orders'))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/update_order_trace/<int:oid>', methods=['POST'])
def update_order_trace(oid):
    if 'user' not in session or session.get('role') != 'Admin':
        return jsonify({"status": "error", "message": "Unauthorized"}), 401
    
    trace = request.form.get('trace')
    if not trace: 
        return jsonify({"status": "error", "message": "Trace value required"}), 400
        
    try:
        conn = get_db_connection()
        cursor = conn.cursor(buffered=True)
        # If trace is 'Delivered', also update status
        if trace == 'Delivered':
            cursor.execute("UPDATE orders SET order_trace = %s, status = 'Delivered' WHERE id = %s", (trace, oid))
        else:
            cursor.execute("UPDATE orders SET order_trace = %s WHERE id = %s", (trace, oid))
        conn.commit()
        cursor.close()
        conn.close()
        flash(f"Order #{oid} tracking updated to {trace}.", "success")
        return redirect(request.referrer or url_for('my_orders'))
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/api/order_status/<int:oid>')
def api_order_status(oid):
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)
        cursor.execute("SELECT status, order_trace FROM orders WHERE id = %s", (oid,))
        order = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if order:
            return jsonify(order)
        return jsonify({"error": "Order not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/user_notifications')
def user_notifications():
    if 'user_id' not in session:
        return jsonify([])
    
    try:
        user_id = session['user_id']
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True, buffered=True)
        # Get recent orders and their current trace
        cursor.execute("SELECT id, order_id, order_trace, status FROM orders WHERE user_id = %s ORDER BY id DESC LIMIT 5", (user_id,))
        updates = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(updates)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- WISHLIST ROUTES ---
@app.route('/wishlist')
def wishlist():
    if 'user_id' not in session:
        return redirect(url_for('login_page'))
    
    user_id = session['user_id']
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    
    # Fetch wishlisted products
    query = """
        SELECT p.* 
        FROM wishlist w
        JOIN product p ON w.product_id = p.id
        WHERE w.user_id = %s
    """
    cursor.execute(query, (user_id,))
    wishlist_products = cursor.fetchall()
    
    cursor.close()
    conn.close()
    return render_template('wishlist.html', products=wishlist_products)

@app.route('/add_to_wishlist', methods=['POST'])
def add_to_wishlist():
    if 'user_id' not in session:
        return jsonify({"status": "error", "message": "Login required"}), 401
    
    data = request.get_json()
    product_id = data.get('product_id')
    user_id = session['user_id']
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor(buffered=True)
        cursor.execute("INSERT INTO wishlist (user_id, product_id) VALUES (%s, %s)", (user_id, product_id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"status": "success", "message": "Added to wishlist"})
    except mysql.connector.Error as err:
        if err.errno == 1062: # Duplicate entry
            return jsonify({"status": "success", "message": "Already in wishlist"})
        return jsonify({"status": "error", "message": str(err)}), 500
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/remove_from_wishlist/<int:pid>', methods=['POST', 'GET'])
def remove_from_wishlist(pid):
    if 'user_id' not in session:
        return redirect(url_for('login_page'))
    
    user_id = session['user_id']
    try:
        conn = get_db_connection()
        cursor = conn.cursor(buffered=True)
        cursor.execute("DELETE FROM wishlist WHERE user_id = %s AND product_id = %s", (user_id, pid))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Product removed from wishlist", "success")
    except Exception as e:
        flash(f"Error removing from wishlist: {str(e)}", "danger")
        
    return redirect(request.referrer or url_for('wishlist'))

@app.route('/cart')
def cart(): return render_template('cart.html')

@app.route('/billing')
def billing():
    return render_template('billing.html')


@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    try:
        data = request.get_json()
        phone = data.get('phone', '').strip().replace(' ', '').replace('-', '')
        message = data.get('message', '')

        if not phone or not message:
            return jsonify({"status": "error", "message": "Phone number and message are required"})

        # Ensure phone number is in E.164 format (e.g., +919876543210)
        if not phone.startswith('+'):
            if len(phone) == 10:
                phone = "+91" + phone
            else:
                return jsonify({"status": "error", "message": "Invalid phone number format. Use +[CountryCode][Number]"})

        # Twilio API
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        message_sent = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone
        )

        print(f"DEBUG Twilio SID: {message_sent.sid}")

        return jsonify({"status": "success", "message": "Receipt sent via Twilio SMS!"})

    except Exception as e:
        print(f"Error in send_sms via Twilio: {e}")
        return jsonify({"status": "error", "message": str(e)})

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/reports')
def reports_page():
    if 'role' not in session or session['role'] != 'Admin':
        return redirect(url_for('login_page'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    
    try:
        # 1. Basic Counts
        cursor.execute("SELECT COUNT(*) as count FROM content")
        total_users = cursor.fetchone()['count']
        
        cursor.execute("SELECT COUNT(*) as count FROM product")
        total_products = cursor.fetchone()['count']
        
        cursor.execute("SELECT COUNT(*) as count FROM category")
        total_categories = cursor.fetchone()['count']
        
        # 2. Sales Metrics
        # Daily Sales
        cursor.execute("SELECT SUM(total_price) as total FROM orders WHERE DATE(order_date) = CURDATE()")
        daily_sales = cursor.fetchone()['total'] or 0
        
        # Monthly Sales
        cursor.execute("SELECT SUM(total_price) as total FROM orders WHERE MONTH(order_date) = MONTH(CURDATE()) AND YEAR(order_date) = YEAR(CURDATE())")
        monthly_sales = cursor.fetchone()['total'] or 0
        
        # 3. Most Purchased Products (Top 5)
        cursor.execute("""
            SELECT item_name, SUM(qty) as total_qty 
            FROM orders 
            GROUP BY item_name 
            ORDER BY total_qty DESC 
            LIMIT 5
        """)
        top_products = cursor.fetchall()

        # 4. Product Sales Table Data
        cursor.execute("""
            SELECT item_name, SUM(qty) as total_qty, SUM(total_price) as total_revenue
            FROM orders
            GROUP BY item_name
            ORDER BY total_revenue DESC
        """)
        product_sales = cursor.fetchall()

        # 5. Low Stock Products (for pie chart and stat card)
        cursor.execute("""
            SELECT product_name, quantity, category, image 
            FROM product 
            WHERE quantity <= %s 
            ORDER BY quantity ASC
        """, (LOW_STOCK_THRESHOLD,))
        low_stock_products = cursor.fetchall()
        low_stock_count_val = len(low_stock_products)

        # 6. Total Suppliers
        try:
            cursor.execute("SELECT COUNT(DISTINCT supplier_name) as count FROM stock_in WHERE supplier_name IS NOT NULL AND supplier_name != ''")
            total_suppliers = cursor.fetchone()['count']
        except Exception:
            total_suppliers = 0

        # 7. Total Orders & Pending Orders
        cursor.execute("SELECT COUNT(*) as count FROM orders")
        total_orders = cursor.fetchone()['count']

        cursor.execute("SELECT COUNT(*) as count FROM orders WHERE status = 'Pending'")
        pending_orders = cursor.fetchone()['count']
        
    except Exception as e:
        print(f"Error in reports data fetching: {e}")
        total_users = total_products = total_categories = 0
        daily_sales = monthly_sales = 0
        top_products = []
        product_sales = []
        low_stock_products = []
        low_stock_count_val = 0
        total_suppliers = 0
        total_orders = 0
        pending_orders = 0
    finally:
        cursor.close()
        conn.close()
    
    return render_template('reports.html', 
                          total_users=total_users,
                          total_products=total_products,
                          total_categories=total_categories,
                          daily_sales=daily_sales,
                          monthly_sales=monthly_sales,
                          top_products=top_products,
                          product_sales=product_sales,
                          low_stock_products=low_stock_products,
                          low_stock_count_val=low_stock_count_val,
                          total_suppliers=total_suppliers,
                          total_orders=total_orders,
                          pending_orders=pending_orders)


@app.route('/predict_sales')
def predict_sales():
    if 'role' not in session or session['role'] != 'Admin':
        return jsonify({"error": "Admin access required"})
    
    conn = get_db_connection()
    # Note: We assume 'orders' table has 'created_at' or we use 'id' as order sequence
    # For robust prediction, real dates are better. If missing, we'll mock some for the demo.
    query = "SELECT item_name, SUM(qty) as total_qty FROM orders GROUP BY item_name"
    df = pd.read_sql(query, conn)
    
    if df.empty:
        return jsonify({"message": "Not enough data for prediction"})

    # Simple trend prediction logic: 
    # In a real app, you'd group by Date. Here we'll generate a forecast based on simple linear growth.
    # For the sake of the requirement, let's provide a structured response.
    import math
    predictions = []
    for index, row in df.iterrows():
        current_sales = float(row['total_qty'])
        # Forecast logic: 50% growth, rounded up to next integer
        forecast = int(math.ceil(current_sales * 1.5))
        
        # Guarantee distinct values for small numbers
        if current_sales > 0 and forecast <= current_sales:
            forecast = int(current_sales + 1)
            
        predictions.append({
            "product": row['item_name'],
            "current_sales": int(current_sales),
            "forecast_next_month": int(forecast)
        })
    
    conn.close()
    return jsonify(predictions)

@app.route('/transactions')
def transactions_page():
    if 'role' not in session or session['role'] != 'Admin':
        return redirect(url_for('login_page'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True, buffered=True)
    
    try:
        # Fetch all orders to show the financial breakdown
        cursor.execute("SELECT * FROM orders ORDER BY id DESC")
        orders = cursor.fetchall()
        
    except Exception as e:
        print(f"Error in transactions data fetching: {e}")
        orders = []
    finally:
        cursor.close()
        conn.close()
    
    return render_template('transactions.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
